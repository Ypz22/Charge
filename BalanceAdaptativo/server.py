import requests
import threading
import json

urls = ['http://127.0.0.1:3000/api?param=482c811da5d5b4bc6d497ffa98491e38', 'http://127.0.0.1:3000/api?param=d8578edf8458ce06fbc5bb76a58c5ca4', 'http://127.0.0.1:3000/api?param=25d55ad283aa400af464c76d713c07ad', 'http://127.0.0.1:3000/api?param=21232f297a57a5a743894a0e4a801fc3', 'http://127.0.0.1:3000/api?param=0d107d09f5bbe40cade3de5c71e9e9b7', 'http://127.0.0.1:3000/api?param=40be4e59b9a2a2b5dffb918c0e86b3d7', 'http://127.0.0.1:3000/api?param=d0763edaa9d9bd2a9516280e9044d885', 'http://127.0.0.1:3000/api?param=e99a18c428cb38d5f260853678922e03', 'http://127.0.0.1:3000/api?param=37b4e2d82900d5e94b8da524fbeb33c0', 'http://127.0.0.1:3000/api?param=4297f44b13955235245b2497399d7a93', 'http://127.0.0.1:3000/api?param=0571749e2ac330a7455809c6b0e7af90', 'http://127.0.0.1:3000/api?param=f25a2fc72690b780b2a14e140ef6a9e0', 'http://127.0.0.1:3000/api?param=5badcaf789d3d1d09794d8f021f40f0e', 'http://127.0.0.1:3000/api?param=827ccb0eea8a706c4c34a16891f84e7b', 'http://127.0.0.1:3000/api?param=8621ffdbc5698829397d97767ac13db3', 'http://127.0.0.1:3000/api?param=5fcfd41e547a12215b173ff47fdd3739', 'http://127.0.0.1:3000/api?param=84d961568a65073a3bcf0eb216b2a576', 'http://127.0.0.1:3000/api?param=ec0e2603172c73a8b644bb9456c1ff6e', 'http://127.0.0.1:3000/api?param=c378985d629e99a4e86213db0cd5e70d', 'http://127.0.0.1:3000/api?param=3bf1114a986ba87ed28fc1b5884fc2f8', 'http://127.0.0.1:3000/api?param=6eea9b7ef19179a06954edd0f6c05ceb', 'http://127.0.0.1:3000/api?param=1c63129ae9db9c60c3e8aa94d3e00495', 'http://127.0.0.1:3000/api?param=c44a471bd78cc6c2fea32b9fe028d30a', 'http://127.0.0.1:3000/api?param=276f8db0b86edaa7fc805516c852c889', 'http://127.0.0.1:3000/api?param=df53ca268240ca76670c8566ee54568a', 'http://127.0.0.1:3000/api?param=8afa847f50a716e64932d995c8e7435a', 'http://127.0.0.1:3000/api?param=eb0a191797624dd3a48fa681d3061212', 'http://127.0.0.1:3000/api?param=c33367701511b4f6020ec61ded352059', 'http://127.0.0.1:3000/api?param=7c6a180b36896a0a8c02787eeafb0e4c', 'http://127.0.0.1:3000/api?param=76419c58730d9f35de7ac538c2fd6737', 'http://127.0.0.1:3000/api?param=49265c16d1dff8acef3499bd889299d6', 'http://127.0.0.1:3000/api?param=f36d238668130c6d9e49448cb64395cf', 'http://127.0.0.1:3000/api?param=f30aa7a662c728b7407c54ae6bfd27d1', 'http://127.0.0.1:3000/api?param=1bfcd4b33578f8af158d851c29b8c422', 'http://127.0.0.1:3000/api?param=45fb45cd49d4fffa0c72db7e59450d4f', 'http://127.0.0.1:3000/api?param=5858ea228cc2edf88721699b2c8638e5', 'http://127.0.0.1:3000/api?param=fea0f1f6fede90bd0a925b4194deac11', 'http://127.0.0.1:3000/api?param=1669972908967b4076b39d4626090817', 'http://127.0.0.1:3000/api?param=46f94c8de14fb36680850768ff1b7f2a', 'http://127.0.0.1:3000/api?param=2ab96390c7dbe3439de74d0c9b0b1767', 'http://127.0.0.1:3000/api?param=5ebe2294ecd0e0f08eab7690d2a6ee69', 'http://127.0.0.1:3000/api?param=ecb2dfbe7d2cb1ee6a0b9862f523cd8e', 'http://127.0.0.1:3000/api?param=0acf4539a14b3aa27deeb4cbdf6e989f', 'http://127.0.0.1:3000/api?param=ef4cdd3117793b9fd593d7488409626d', 'http://127.0.0.1:3000/api?param=b3f952d5d9adea6f63bee9d4c6fceeaa', 'http://127.0.0.1:3000/api?param=10afb095c2d6ecbb5c415ba8099486b9', 'http://127.0.0.1:3000/api?param=6f4ec514eee84cc58c8e610a0c87d7a2', 'http://127.0.0.1:3000/api?param=29341d821efefb7511ad870d61d6e360', 'http://127.0.0.1:3000/api?param=527f5a7b2e27b567266b89818d3376c5', 'http://127.0.0.1:3000/api?param=bcd84f092e56e618f4a5736e465cd1a7', 'http://127.0.0.1:3000/api?param=2dc4b6336da6c9ba6bdfd2b0eb95f2eb', 'http://127.0.0.1:3000/api?param=941eda68f5a6fd2b941d201ea5ccd8cf', 'http://127.0.0.1:3000/api?param=47d9c631aeafd9cdbdaa6ec195bbea45', 'http://127.0.0.1:3000/api?param=27b75f2a5b87b68dd1416bf425b92f9b', 'http://127.0.0.1:3000/api?param=85385e42b9dd09e664fa01f7e9a4d998', 'http://127.0.0.1:3000/api?param=8259f0b42fb9589b5d169d15c4868311', 'http://127.0.0.1:3000/api?param=594a49d3be2e3ad2f57005a21820763e', 'http://127.0.0.1:3000/api?param=76247aa53de86ce67d5915244b3e862f', 'http://127.0.0.1:3000/api?param=b698e3c111760687ef9e4d0cff6e51b6', 'http://127.0.0.1:3000/api?param=ea5e4db68ee287d4ac82bbf4a05d4c93', 'http://127.0.0.1:3000/api?param=981c667f25d79d140fa35fe5efbcef0a', 'http://127.0.0.1:3000/api?param=be5acd513f2f05de7ba5a674a2444c6f', 'http://127.0.0.1:3000/api?param=ec230d33dd1a8e9ea2e5e7aee9d07c9e', 'http://127.0.0.1:3000/api?param=3bf773623cb161a0de2dfeb3d3095f2c', 'http://127.0.0.1:3000/api?param=83a312f9f56b65011e78a31edfbc1490', 'http://127.0.0.1:3000/api?param=6512a6ddfe4800c18a4be4139de8d0b3', 'http://127.0.0.1:3000/api?param=a802a0667469b6992b7de887b0182375', 'http://127.0.0.1:3000/api?param=10c2d330177d2da1d9c256f8e86c6228', 'http://127.0.0.1:3000/api?param=e2328e2f0df645fbc210b9b66faa8c01', 'http://127.0.0.1:3000/api?param=dd23820eda41cd067d28584c14832134', 'http://127.0.0.1:3000/api?param=efa4124d7283953b40d472d47cdf1580', 'http://127.0.0.1:3000/api?param=f026feffc4bfeea4b3d0367c41e4d2a4', 'http://127.0.0.1:3000/api?param=6dff48616b97796988acebc454f41d84', 'http://127.0.0.1:3000/api?param=5c3c55bf2610e42effa6d374408885f3', 'http://127.0.0.1:3000/api?param=0cdf40a28480979ae204458ce79138c1', 'http://127.0.0.1:3000/api?param=7917b0cd9611af6586ffbf19eb5df45d', 'http://127.0.0.1:3000/api?param=526b4d449bc62bd42e9eacbf4f607cb3', 'http://127.0.0.1:3000/api?param=f0d3b57b62b5b0b29d66f67bac7ab98c', 'http://127.0.0.1:3000/api?param=8be4f31977e92dd793b12321a3f45782', 'http://127.0.0.1:3000/api?param=42fd690a80a6310f47a32a66ff1329c3', 'http://127.0.0.1:3000/api?param=57586cf6679f824abd9e2114c1abbe4e', 'http://127.0.0.1:3000/api?param=7ff45fcba0c7becbff5df81b433c7fb6', 'http://127.0.0.1:3000/api?param=72aed94e971063a312e07f6ff6f53f04', 'http://127.0.0.1:3000/api?param=21688b7cefbccf0c2351e25b982b7dca', 'http://127.0.0.1:3000/api?param=bf73c31595ef3ef59d508636261c1213', 'http://127.0.0.1:3000/api?param=5e1deffb678ed723d04c3b7196d08f90', 'http://127.0.0.1:3000/api?param=5c25407fa946108e8570f08b6fe81995', 'http://127.0.0.1:3000/api?param=25edea8ce74ded5576493f8d70c44282', 'http://127.0.0.1:3000/api?param=7ef7b8dc26e32992fa76b430b599eb45', 'http://127.0.0.1:3000/api?param=efad29c10052f3cfeb4f95cb8a11f255', 'http://127.0.0.1:3000/api?param=4870a8e25f526e8da45635890a647220', 'http://127.0.0.1:3000/api?param=5fba04c79840c8017ebc65e47e2fd857', 'http://127.0.0.1:3000/api?param=3bbf8ac449cbe752241a52f46adbdc6c', 'http://127.0.0.1:3000/api?param=672a3b991224dd23cdc49f5ee441d2c8', 'http://127.0.0.1:3000/api?param=1a7e8da51e32543083c8b5f758b1e3e0', 'http://127.0.0.1:3000/api?param=ae37a0f10c09d978060fded102a98cd4', 'http://127.0.0.1:3000/api?param=0de6021a1c9698f62c0febffb3eeb949', 'http://127.0.0.1:3000/api?param=139b768f69e7714cb395d98160032f07', 'http://127.0.0.1:3000/api?param=f8c6e75d8a643586172c6f85e0b5af48', 'http://127.0.0.1:3000/api?param=c6fbc6d7d98f27f69efa5d2b65984eba', 'http://127.0.0.1:3000/api?param=421587135da1cafee7bb5a9b01443441', 'http://127.0.0.1:3000/api?param=ba6e7acc3d9e728fa7c3d9c0879e463c', 'http://127.0.0.1:3000/api?param=1396b21be9195a8b51ac134e29fa7836', 'http://127.0.0.1:3000/api?param=a7a3aa98844ae48b7f41a5f2b70abe9f', 'http://127.0.0.1:3000/api?param=61e861e6a3dbafc35c0120c0ba0d3d41', 'http://127.0.0.1:3000/api?param=ce17b9b26d25a3b87271366976a0e3ba', 'http://127.0.0.1:3000/api?param=34e7d81b4eb28669f8987dee2dad721b', 'http://127.0.0.1:3000/api?param=2d71993d153a7fa8f14e3ecc71be068d', 'http://127.0.0.1:3000/api?param=669960670ef18f477cfcec11cf9ce4df', 'http://127.0.0.1:3000/api?param=4a43ddeb5a5faf352a0b66c5d3e0ac63', 'http://127.0.0.1:3000/api?param=ea173b4ac7ea92ea54a1a9e17afd80d0', 'http://127.0.0.1:3000/api?param=dd85be0c520663ba9c74b538657a84f3', 'http://127.0.0.1:3000/api?param=6ce576d7c3ae97a24b0de4dde46ad607', 'http://127.0.0.1:3000/api?param=f36911fd4d406e7b5e2e77c03b9581d8', 'http://127.0.0.1:3000/api?param=52fde792a87ccc155110c514899f1ca2', 'http://127.0.0.1:3000/api?param=24de975b6e2315ecc551da9900457163', 'http://127.0.0.1:3000/api?param=8e5e2a248474222b4790e8fd0d27b12a', 'http://127.0.0.1:3000/api?param=fa685c9c9bcff80cfd74dc80e697c5b3', 'http://127.0.0.1:3000/api?param=1861704fe143c5a72248aefc50737527', 'http://127.0.0.1:3000/api?param=496ddf669cf7e3b6d25a32a8b0e5b169', 'http://127.0.0.1:3000/api?param=d1456291418ebc5354af02cc74af50d7', 'http://127.0.0.1:3000/api?param=aada4f1b19b37ea4f383b4046bb906df', 'http://127.0.0.1:3000/api?param=066936c0f7e2c113ac8f03e78fdee2d5', 'http://127.0.0.1:3000/api?param=40a221a8b79768fafae7c140f7f062f3', 'http://127.0.0.1:3000/api?param=705b5e25b6881d57fa2b3da234308b23', 'http://127.0.0.1:3000/api?param=2af17fc6f4ddb905c90b743dda9f5985', 'http://127.0.0.1:3000/api?param=a9944f19a7097d8c11010e835957c94d', 'http://127.0.0.1:3000/api?param=1cd2a0462c600cfde664da87822379b2', 'http://127.0.0.1:3000/api?param=d1ec12e5cdba8bf84feffd77fd656374', 'http://127.0.0.1:3000/api?param=64f37beafffbb552ae716b090859642d', 'http://127.0.0.1:3000/api?param=a2a530f8c684cbc4b18e3ebbd9bde1b4', 'http://127.0.0.1:3000/api?param=a74db9ebd271eccf0b10cda012603079', 'http://127.0.0.1:3000/api?param=ea7b22e025b9af5b0a2703cf8f57d55f', 'http://127.0.0.1:3000/api?param=80570942df306da01242058e4076ef40', 'http://127.0.0.1:3000/api?param=6cc4fa209f848bb2478e4e8e7d2502cf', 'http://127.0.0.1:3000/api?param=77d812c34c13d7ab5a6c25c1b780c841', 'http://127.0.0.1:3000/api?param=f5b57521ec7f8363fe50bd981fbe3390', 'http://127.0.0.1:3000/api?param=18676b0dcb438e6dda04d37219146e27', 'http://127.0.0.1:3000/api?param=52a5510a8b23d97f3bf144a80aec1952', 'http://127.0.0.1:3000/api?param=a1f7fc8ee7164e11621f979712440c01', 'http://127.0.0.1:3000/api?param=198e7ba0125273319cc2ce445e09c7b4', 'http://127.0.0.1:3000/api?param=9e29ec73e8e3e7fa5e94770964c930f2', 'http://127.0.0.1:3000/api?param=afd5c437fa8b17115ad3eeec53c7b615', 'http://127.0.0.1:3000/api?param=b3680618397d587e9d3552a0cef4d9f5', 'http://127.0.0.1:3000/api?param=ac61d71503e7eb4e971ae2e7d1cd42f8', 'http://127.0.0.1:3000/api?param=83f32d1e82f90ac70b8a609f91188420', 'http://127.0.0.1:3000/api?param=aacccaf5262e54d077fcdff311132280', 'http://127.0.0.1:3000/api?param=67a181b5918f12fdef28387ef639e0e6', 'http://127.0.0.1:3000/api?param=6acb9d3954f40a444aee5e71c1b9956c', 'http://127.0.0.1:3000/api?param=47588c906922606f2e9eb444e5988d75', 'http://127.0.0.1:3000/api?param=c6eec6a82d50f3b2196f37babd0410ad', 'http://127.0.0.1:3000/api?param=abef778526992729ede6c47916d803af', 'http://127.0.0.1:3000/api?param=c7df96d8043c5f6d9a1abb14573fb50c', 'http://127.0.0.1:3000/api?param=63acc346f381d1282a9e9a4d5cd11b49', 'http://127.0.0.1:3000/api?param=15ac73e6984c718c1ed009eed4afb9cf', 'http://127.0.0.1:3000/api?param=0f3f8270b8a623f17fb02b1ded112d98', 'http://127.0.0.1:3000/api?param=f43b0d8d296123389179c253e061396c', 'http://127.0.0.1:3000/api?param=8efb7021c16334a3b5f7e263c44fefbd', 'http://127.0.0.1:3000/api?param=3609d3eb4e497454f692593e481cd5a8', 'http://127.0.0.1:3000/api?param=0076020c8cd9d19f6091ab9da48205fe', 'http://127.0.0.1:3000/api?param=ae6e81cd8094482d70a2047f13fdc36a', 'http://127.0.0.1:3000/api?param=75ea7aeb2f33d61a7ab9f4c38fea62a8', 'http://127.0.0.1:3000/api?param=b309dc97d76f8d727162d4e068742770', 'http://127.0.0.1:3000/api?param=4317b239b4d47ad9a0fbe3b51ed2f486', 'http://127.0.0.1:3000/api?param=0d6c762e4b9c05877946c6b0a6af5023', 'http://127.0.0.1:3000/api?param=ef449131ecc776f715e474a0b62b2009', 'http://127.0.0.1:3000/api?param=76ac4bd48a9676356960dc59b938eee4', 'http://127.0.0.1:3000/api?param=fb608a0a5ebe0345f5bde141c7f12bd2', 'http://127.0.0.1:3000/api?param=c4bb99ec336346888102b371ac36bc61', 'http://127.0.0.1:3000/api?param=7e60917afeb03cd598ec48943db55ced', 'http://127.0.0.1:3000/api?param=929e567bfb1132d255acf9a79eedd125', 'http://127.0.0.1:3000/api?param=f6253ca280d74bc09feda276eb0b0813', 'http://127.0.0.1:3000/api?param=f61675de914ba0d8a49fe457fec9c3b8', 'http://127.0.0.1:3000/api?param=60bf78f5a435b27760bc054e21ae9ef5', 'http://127.0.0.1:3000/api?param=da8b3473aded58d62934ba09c41949be', 'http://127.0.0.1:3000/api?param=31d029c886fe8466853fcb73290c29ee', 'http://127.0.0.1:3000/api?param=4140f9d03e3436e9eb2f2d291c9b3504', 'http://127.0.0.1:3000/api?param=784ad5735a9953df8a43d06718f21c3b']

MASTER_URL = "http://127.0.0.1:3000/add_task"

def send_task(url):
    try:
        # Extraer el hash desde la URL
        param = url.split("param=")[-1]

        # Construir el JSON con los datos correctos
        task_data = {
            "hash": param,
            "hash_type": "md5",  # Puedes cambiarlo según sea necesario
            "dictionary": "dic.txt"  # Nombre del diccionario
        }

        # Enviar la tarea al servidor master
        response = requests.post(MASTER_URL, json=task_data)

        # Verificar respuesta del servidor
        if response.status_code == 200:
            print(f"✅ Tarea enviada con éxito: {param}")
        else:
            print(f"❌ Error al enviar tarea {param}: {response.json()}")
    except Exception as e:
        print(f"❌ Error en la solicitud para {param}: {e}")

# Crear y ejecutar hilos para enviar las tareas más rápido
threads = []
for url in urls:
    thread = threading.Thread(target=send_task, args=(url,))
    threads.append(thread)
    thread.start()

# Esperar a que todas las tareas sean enviadas
for thread in threads:
    thread.join()

print("🚀 Todas las tareas han sido enviadas correctamente.")