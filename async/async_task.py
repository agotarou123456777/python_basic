import asyncio
import random
import aioconsole

async def _as_task_movie_query(idx):
    timer = random.uniform(0.1, 2)
    
    await asyncio.sleep(timer)

    result = "===== task id {} is awake! =====".format(idx)
    return result

async def read_key_input(queue):
    while True:
        key = await aioconsole.ainput()
        await queue.put(key)
        if key == 'q':
            break

async def _as_watcher_task(tasks, idx, timeout):
    
    new_task = asyncio.create_task(_as_task_movie_query(idx))
    tasks.append(new_task)
    
    try:
        result = await asyncio.wait_for(new_task, timeout=timeout)
        print(result)
        tasks.remove(new_task)
        return True
        
    except asyncio.TimeoutError:
        print("The task took too long and was cancelled.")
        new_task.cancel()
        return False
        
        

async def _as_main_task_manager(queue):
    

    delay = 0.5
    timeout = 600
    
    tasks = []
    task_id = 0
    
    
    
    while True:        
        
        if not queue.empty():
            key = await queue.get()
            print(f"Received key: {key}")
            if key == 'q':
                print("Exiting...")
                break
            
            if key == 'c':
                print("Creaing Task...")
                new_watcher_task = asyncio.create_task(_as_watcher_task(tasks, task_id,timeout=timeout))
                task_id += 1
                         
        
        await asyncio.sleep(delay)
        
        print("task manager loop")


    # すべてのタスク完了を待って終了
    if tasks:
        done, pending = await asyncio.wait(tasks) 
    
        print("Done tasks:")
        for task in done:
            print(task.result())
        
        print("Pending tasks:")
        for task in pending:
            print(task)
    
    print("All tasks completed")



async def _as_main():
    
    queue = asyncio.Queue()
    
    input_task = asyncio.create_task(read_key_input(queue))
    process_task = asyncio.create_task(_as_main_task_manager(queue))
    
    await asyncio.gather(input_task, process_task)


if __name__=="__main__":  
    asyncio.run(_as_main())