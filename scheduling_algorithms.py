
class SchedulingAlgorithms:
    @staticmethod
    def simulate_fcfs(processes):
        # Sort by arrival time
        procs = sorted(processes, key=lambda x: x['at'])
        current_time = 0
        schedule = []
        total_tat = 0
        total_wt = 0

        for p in procs:
            if current_time < p['at']:
                current_time = p['at'] 
            
            start_time = current_time
            current_time += p['bt']
            
            tat = current_time - p['at']
            wt = tat - p['bt']
            
            total_tat += tat
            total_wt += wt
            
            schedule.append((p['name'], start_time, current_time))

        num_of_processes = len(procs)
        return schedule, total_tat / num_of_processes, total_wt / num_of_processes

    @staticmethod
    def simulate_rr(processes, tq):
        # Sort by arrival time
        procs = sorted(processes, key=lambda x: x['at'])
        num_of_processes = len(procs)
        current_time = 0
        schedule = []
        completed = 0
        completion_times = {}
        ready_queue = []
        idx = 0

        while idx < num_of_processes and procs[idx]['at'] <= current_time:
            ready_queue.append(procs[idx])
            idx += 1

        if not ready_queue and idx < num_of_processes:
            current_time = procs[idx]['at']
            ready_queue.append(procs[idx])
            idx += 1

        while completed < num_of_processes:
            if not ready_queue:
                current_time = procs[idx]['at']
                while idx < num_of_processes and procs[idx]['at'] <= current_time:
                    ready_queue.append(procs[idx])
                    idx += 1

            p = ready_queue.pop(0)
            start_time = current_time
            
            time_processed = min(p['rem_bt'], tq)
            p['rem_bt'] -= time_processed
            current_time += time_processed
            
            schedule.append((p['name'], start_time, current_time))

            while idx < num_of_processes and procs[idx]['at'] <= current_time:
                ready_queue.append(procs[idx])
                idx += 1

            if p['rem_bt'] > 0:
                ready_queue.append(p)
            else:
                completed += 1
                completion_times[p['name']] = current_time

        total_tat = 0
        total_wt = 0
        for p in processes:
            tat = completion_times[p['name']] - p['at']
            wt = tat - p['bt']
            total_tat += tat
            total_wt += wt

        return schedule, total_tat / num_of_processes, total_wt / num_of_processes
    
    @staticmethod
    def simulate_sjf(processes):
        num_of_processes = len(processes)
        completed = 0
        current_time = 0
        schedule = []
        total_tat = 0
        total_wt = 0
        
        # Keep track of which processes are finished so we don't pick them again
        is_completed = {p['name']: False for p in processes}
        
        while completed < num_of_processes:
            # Gather all processes that have arrived and are not finished
            available = [p for p in processes if p['at'] <= current_time and not is_completed[p['name']]]
            
            if not available:
                # If no one has arrived yet, jump the clock forward to the next arrival time (Idle CPU)
                next_arrival = min([p['at'] for p in processes if not is_completed[p['name']]])
                current_time = next_arrival
                continue
            
            # Sort the available processes by Burst Time. 
            # If there's a tie, fall back to Arrival Time.
            available.sort(key=lambda x: (x['bt'], x['at']))
            p = available[0] # Pick the shortest
            
            # Execute the process
            start_time = current_time
            current_time += p['bt']
            is_completed[p['name']] = True
            completed += 1
            
            # Calculate metrics
            tat = current_time - p['at']
            wt = tat - p['bt']
            total_tat += tat
            total_wt += wt
            
            schedule.append((p['name'], start_time, current_time))
            
        return schedule, total_tat / num_of_processes, total_wt / num_of_processes