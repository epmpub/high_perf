import asyncio
import aiohttp
import blog_spider


async def async_craw(url):
    print(f"craw url:{url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            result = await resp.text()
            print(f"craw url:{url},{len(result)}")


loop = asyncio.get_event_loop()

urls = [
    f"https://www.cnblogs.com/#p{page}"
    for page in range(1, 50 + 1)
]


if __name__ == '__main__':
    tasks = [
        loop.create_task(async_craw(url))
        for url in blog_spider.urls]

    import time

    start = time.time()
    loop.run_until_complete(asyncio.wait(tasks))
    end = time.time()
    print("use time seconds:", end-start)

