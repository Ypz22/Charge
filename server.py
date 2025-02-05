import requests
import concurrent.futures

urls = [
    "http://127.0.0.1:3000/api?param=482c811da5d5b4bc6d497ffa98491e38",
    "http://127.0.0.1:3000/api?param=d8578edf8458ce06fbc5bb76a58c5ca4",
    "http://127.0.0.1:3000/api?param=25d55ad283aa400af464c76d713c07ad",
    "http://127.0.0.1:3000/api?param=21232f297a57a5a743894a0e4a801fc3",
    "http://127.0.0.1:3000/api?param=0d107d09f5bbe40cade3de5c71e9e9b7",
    "http://127.0.0.1:3000/api?param=5f4dcc3b5aa765d61d8327deb882cf99",
    "http://127.0.0.1:3000/api?param=d0763edaa9d9bd2a9516280e9044d885",
    "http://127.0.0.1:3000/api?param=e99a18c428cb38d5f260853678922e03",
    "http://127.0.0.1:3000/api?param=37b4e2d82900d5e94b8da524fbeb33c0",
    "http://127.0.0.1:3000/api?param=4297f44b13955235245b2497399d7a93",
    "http://127.0.0.1:3000/api?param=f25a2fc72690b780b2a14e140ef6a9e0",
    "http://127.0.0.1:3000/api?param=f3d017ffbb74cf6c514e9818f7c7b3f4",
    "http://127.0.0.1:3000/api?param=f7c3bc1d808e04732adf679965ccc34ca7ae3441",
    "http://127.0.0.1:3000/api?param=827ccb0eea8a706c4c34a16891f84e7b",
    "http://127.0.0.1:3000/api?param=8621ffdbc5698829397d97767ac13db3",
    "http://127.0.0.1:3000/api?param=b9c2f99e8fef91032e7b431f3d1c123e",
    "http://127.0.0.1:3000/api?param=06d577fea93271c3c2d9cd070bb8c81b",
    "http://127.0.0.1:3000/api?param=0be62eb39627fa6353cc24fbc3a6ee80",
    "http://127.0.0.1:3000/api?param=64612e86b8ad13b5687a5cbbda6f3a1f",
    "http://127.0.0.1:3000/api?param=0c75f31cfd496d71d7e931badf43c051",
    "http://127.0.0.1:3000/api?param=20b14727c838db7a14f1d4a1aa1dd460",
    "http://127.0.0.1:3000/api?param=7b8b965ad4bca0e41ab51de7b31363a1",
    "http://127.0.0.1:3000/api?param=b4b147bc522828731f1a016bfa72c073",
    "http://127.0.0.1:3000/api?param=e29cc7b4cd94b76a7be68320686b6b3f",
    "http://127.0.0.1:3000/api?param=7b4b21745f941bbe6a99d39a9811b2fd",
    "http://127.0.0.1:3000/api?param=a7ee0b3783db9d0c4b5f7c5f78d6f4aa",
    "http://127.0.0.1:3000/api?param=e72e16c1e47a28cf5621398e35e5fb96",
    "http://127.0.0.1:3000/api?param=c33367701511b4f6020ec61ded352059",
    "http://127.0.0.1:3000/api?param=7c6a180b36896a0a8c02787eeafb0e4c",
    "http://127.0.0.1:3000/api?param=8966b9440b1737f03dc3791d86b08391",
    "http://127.0.0.1:3000/api?param=f27e6a609a40747510d3c0fe11fa6f65",
    "http://127.0.0.1:3000/api?param=5ed94a66f29be7d290260c36526a1c01",
    "http://127.0.0.1:3000/api?param=4001ec6dd1e7a573ee2f5e8dcf5e7e0c",
    "http://127.0.0.1:3000/api?param=24ebcbbe91cd872bf08edb70f44cfb82",
    "http://127.0.0.1:3000/api?param=900150983cd24fb0d6963f7d28e17f72",
    "http://127.0.0.1:3000/api?param=b58e03b3c7db24e4ff7f8295b9b89b86",
    "http://127.0.0.1:3000/api?param=8f29a4fa7cbb476d135a005ebfb55a4b",
    "http://127.0.0.1:3000/api?param=15de21c670ae7c3f6f3f1f37029303c9",
    "http://127.0.0.1:3000/api?param=15c17685c60c2321de242c35a90a4b6b",
    "http://127.0.0.1:3000/api?param=3c0a7ce3a6db7d0a32ff18a65b579d60",
    "http://127.0.0.1:3000/api?param=5ebe2294ecd0e0f08eab7690d2a6ee69",
    "http://127.0.0.1:3000/api?param=8bd6e99b4dfdfcc884ef57a096bdcd5d",
    "http://127.0.0.1:3000/api?param=0c307e7fc3914dc09e03e484a3e6a21f",
    "http://127.0.0.1:3000/api?param=4b21a682f28e8d89b174f957ea0fbd3e",
    "http://127.0.0.1:3000/api?param=09c5a10b5ee8662e16404a5d63a9576f",
    "http://127.0.0.1:3000/api?param=5f367dcf2db7195efcc383603c6092c4",
    "http://127.0.0.1:3000/api?param=7b774effe4a349c6dd82ad4f4f21d34c",
]

def fetch(url):
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(fetch, urls))

print("Resultados:", results)
