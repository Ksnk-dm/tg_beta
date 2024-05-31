import asyncio
import aiomysql
import ssl

async def test_connection():
    conn = await aiomysql.connect(host='uashared27.twinservers.net', port=2083,
                                  user='ksnktech_tg_user',password='=i,F4WlM^bO.=', db='ksnktech_tg')
    print("Соединение установлено")
    async with conn.cursor() as cur:
        # Вставка нового значения в таблицу users
        await cur.execute("INSERT INTO users (user_id, phone) VALUES (%s, %s)", ("355345", "phone"))
        await conn.commit()  # Подтверждение изменений
    conn.close()

#  loop = asyncio.get_event_loop()
# loop.run_until_complete(test_connection(loop))
asyncio.run(test_connection())

