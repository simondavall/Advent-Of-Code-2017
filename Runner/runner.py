import time
import subprocess

failed = []
total_solutions = 25
start = time.perf_counter()
success_count = 0
solution_timings = {}

for day in range(1, total_solutions + 1):
    solution_start = time.perf_counter()
    result = subprocess.run(['pypy3', f'Day{day:02d}/program.py', f'Day{day:02d}/input.txt'], capture_output=True, text=True)
    solution_end = time.perf_counter()
    solution_elapsed = (solution_end - solution_start) * 1000
    solution_timings[day] = solution_elapsed

    if result.returncode == 0:
        success_count += 1
        print(result.stdout)
    else:
        failed.append(day)
        print("Script failed:")
        print(result.stderr) 

end = time.perf_counter()
elapsed_s = (end - start)
print(f"All solutions ran in {elapsed_s:.3f}s. {success_count}/{total_solutions} solutions passed successfully!.")
if (len(failed) > 0):
    print(f"{len(failed)} solutions failed.")
    print(f"Failed solutions (by day): {failed}")


print("\n# Execution Time Summary #")
sorted_timings = dict(sorted(solution_timings.items(), key=lambda item: item[1], reverse=True))
for k, v in sorted_timings.items():
    print(f"Day{k:02d}: {v:.03f}ms")

