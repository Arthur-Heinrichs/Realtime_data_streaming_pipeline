from kafka import KafkaConsumer
import json

topic = "client_plataform_usage"

consumer = KafkaConsumer(
topic #tópico que irá consumir,
api_version=(3,8,0),
bootstrap_servers="kafka:9092",#depende de onde o broker do kafka estiver,
auto_offset_reset="earliest",#le desde o início do tópico se não encontrar um offset
enable_auto_commit=True,
group_id="client_plataform_usage",
value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

if __name__=='__main__':
    for message in consumer:
        print(f"Received: {message.value}")