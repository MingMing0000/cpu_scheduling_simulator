
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

        n = len(procs)
        return schedule, total_tat / n, total_wt / n

    @staticmethod
    def simulate_rr(processes, tq):
        # Sort by arrival time
        procs = sorted(processes, key=lambda x: x['at'])
        n = len(procs)
        current_time = 0
        schedule = []
        completed = 0
        completion_times = {}
        ready_queue = []
        idx = 0

        while idx < n and procs[idx]['at'] <= current_time:
            ready_queue.append(procs[idx])
            idx += 1

        if not ready_queue and idx < n:
            current_time = procs[idx]['at']
            ready_queue.append(procs[idx])
            idx += 1

        while completed < n:
            if not ready_queue:
                current_time = procs[idx]['at']
                while idx < n and procs[idx]['at'] <= current_time:
                    ready_queue.append(procs[idx])
                    idx += 1

            p = ready_queue.pop(0)
            start_time = current_time
            
            time_processed = min(p['rem_bt'], tq)
            p['rem_bt'] -= time_processed
            current_time += time_processed
            
            schedule.append((p['name'], start_time, current_time))

            while idx < n and procs[idx]['at'] <= current_time:
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

        return schedule, total_tat / n, total_wt / n