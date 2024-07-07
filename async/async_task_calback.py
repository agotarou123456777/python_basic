import asyncio
from functools import partial
import random
import aioconsole

async def _as_long_task(idx):
    timer = random.uniform(0.1, 2)
    
    await asyncio.sleep(timer)

    result = "awake"
    ret = [result, idx]
    return ret

async def _as_read_key_input(queue):
    while True:
        key = await aioconsole.ainput()
        await queue.put(key)
        if key == 'q':
            break


def handle_task_callback(task_f, tasks, idx):
    result = task_f.result()
    text, idx = result
    print("********************************************************************************************************************")
    print("id : {}".format(idx))
    print("response : {}".format(result))
    print("********************************************************************************************************************")
    tasks.remove(task_f)
    return result


async def _as_main_task_manager(queue):
    
    tasks = []
    task_id = 0
    delay = 0.5

    while True:        
        
        if not queue.empty():
            key = await queue.get()
            print(f"Received key: {key}")
            if key == 'q':
                print("Exiting...")
                break
            
            if key == 'c':
                print("Creaing Task...")

                new_task = asyncio.create_task(_as_long_task(task_id))
                new_task.add_done_callback(partial(handle_task_callback, tasks=tasks, idx = task_id))
                tasks.append(new_task)
                task_id += 1

                         
        
        await asyncio.sleep(delay)
        
        print("task manager loop")

    
    done, pending = await asyncio.wait(tasks) # すべてのタスク完了を待って終了
    
    print("Done tasks:")
    for task in done:
        print(task.result())
    
    print("Pending tasks:")
    for task in pending:
        print(task)
    
    print("All tasks completed")



async def _as_main():
    
    queue = asyncio.Queue()
    
    input_task = asyncio.create_task(_as_read_key_input(queue))
    process_task = asyncio.create_task(_as_main_task_manager(queue))
    
    await asyncio.gather(input_task, process_task)


if __name__=="__main__":  
    asyncio.run(_as_main())