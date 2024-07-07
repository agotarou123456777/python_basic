
import time

counter=30

start_time = time.perf_counter()
try:
    while True:
        counter-=1
        rev=1/counter
        execution_time = time.perf_counter() - start_time
        print("\r"+"counter {} : excution time {:.2}".format(counter, execution_time), end="")
        time.sleep(0.1)
        
except KeyboardInterrupt:
    print("ctrl+C pressed...")
    pass

except ZeroDivisionError:
    print("Zero-division...")

finally:
    print("final")

print("fin")