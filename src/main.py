import asyncio
from tasks import send_email

async def main():
    print("Start the process")
    
    task = send_email.delay("example@gmail.com")
    print(f"Task ID pushed to Queue: {task.id}")

    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, task.get)
    print(f"Returned Result: {result}")

    print("End the process")

if __name__ == "__main__":
    asyncio.run(main())