
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

    