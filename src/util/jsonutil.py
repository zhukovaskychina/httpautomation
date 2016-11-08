# -*- coding: UTF-8 -*-
'''

@author: water
'''
from log.Log import Log
import json
import re

def strToDict(data):
        result = {}
        try:
            temp = re.compile(':null')
            data = temp.sub(":'empty'",data)
            temp = re.compile(':false')
            data = temp.sub(':False',data)
            temp = re.compile(':true')
            data = temp.sub(':True',data)
            result = eval(data)
        except BaseException, e:
            Log.debug(data)
            Log.debug("strToDict exception",  e)
        return result
    
def strToJson(data):
    try:
        datajson = json.loads(data)
    except BaseException, e:
        Log.debug("strToJson",  e)
        print e
        datajson = {}
    return datajson

def dictToStr(data):
    return str(data)

if __name__ == "__main__":
    x = '''{"code":1,"rows":23,"pages":4,"data":[{"song_id":1225886,"singer_id":12649,"song_name":"Moonshadow","singer_name":"Cat Stevens","album_name":"Icon","pick_count":6,"vip":0,"audition_list":[{"duration":"02:50","format":"mp3","bitrate":320,"type_description":"超高品质","url":"http://nie.dfe.yymommy.com/cd0a36745d544923/1415675062/mp3_190_12/c8/51/c8a13287b34ec9991b9a84c1ae25c551.mp3?s=t","size":"6.50M","type":5},{"duration":"02:50","format":"mp3","bitrate":128,"type_description":"标准品质","url":"http://ws.cs.hotchanson.com/5ccf100ca11f1b28/1415675062/mp3_128_12/41/7f/4139b95510c5bd25eba690381defb37f.mp3?s=t","size":"2.60M","type":3},{"duration":"02:50","format":"m4a","bitrate":32,"type_description":"压缩品质","url":"http://oen.cye.yymommy.com/5ccf100ca11f1b28/1415675062/m4a_32_12/41/7f/4139b95510c5bd25eba690381defb37f.m4a?s=t","size":"0.67M","type":1}],"url_list":[{"duration":"02:50","format":"mp3","bitrate":320,"type_description":"超高品质","url":"http://nie.dfe.yymommy.com/cd0a36745d544923/1415675062/mp3_190_12/c8/51/c8a13287b34ec9991b9a84c1ae25c551.mp3?s=t","size":"6.50M","type":5},{"duration":"02:50","format":"mp3","bitrate":128,"type_description":"标准品质","url":"http://ws.cs.hotchanson.com/5ccf100ca11f1b28/1415675062/mp3_128_12/41/7f/4139b95510c5bd25eba690381defb37f.mp3?s=t","size":"2.60M","type":3},{"duration":"02:50","format":"m4a","bitrate":32,"type_description":"压缩品质","url":"http://oen.cye.yymommy.com/5ccf100ca11f1b28/1415675062/m4a_32_12/41/7f/4139b95510c5bd25eba690381defb37f.m4a?s=t","size":"0.67M","type":1}],"ll_list":[{"duration":"02:50","format":"flac","bitrate":850,"type_description":"无损品质","url":"http://nie.dfe.yymommy.com/00d500a53f191b58/1415675062/flac_190_12/16/b6/161cd13fc2272973bf5d677ea30fd3b6.flac?s=t","size":"17.28M"}]},{"song_id":26892287,"singer_id":12649,"song_name":"Moonshadow ","singer_name":"Cat Stevens","album_name":"Greatest Hits","pick_count":0,"vip":0,"audition_list":[{"duration":"02:50","format":"mp3","bitrate":128,"type_description":"标准品质","url":"http://nmo.ouj.yymommy.com/778dd7aa1a3d9e32/1415675062/mp3_128_268/e9/be/e93528de4515c0aa2acf280c002391be.mp3?s=t","size":"2.61M","type":3},{"duration":"02:50","format":"m4a","bitrate":32,"type_description":"压缩品质","url":"http://a.ali.dongting.com/778dd7aa1a3d9e32/1415675062/m4a_32_268/e9/be/e93528de4515c0aa2acf280c002391be.m4a?s=t","size":"0.67M","type":1}],"url_list":[{"duration":"02:50","format":"mp3","bitrate":128,"type_description":"标准品质","url":"http://nmo.ouj.yymommy.com/778dd7aa1a3d9e32/1415675062/mp3_128_268/e9/be/e93528de4515c0aa2acf280c002391be.mp3?s=t","size":"2.61M","type":3},{"duration":"02:50","format":"m4a","bitrate":32,"type_description":"压缩品质","url":"http://a.ali.dongting.com/778dd7aa1a3d9e32/1415675062/m4a_32_268/e9/be/e93528de4515c0aa2acf280c002391be.m4a?s=t","size":"0.67M","type":1}]},{"song_id":3398002,"singer_id":66987,"song_name":"Moonshadow","singer_name":"欧美群星","album_name":" ","pick_count":0,"vip":0,"audition_list":[{"duration":"02:50","format":"m4a","bitrate":96,"type_description":"标准品质","url":"http://b.ali.hotchanson.com/f66db30f9c4296f7/1415675062/m4a_96_33/78/52/7869347cb0ec4d7e2570812d02425452.m4a?s=t","size":"1.96M","type":2},{"duration":"02:51","format":"m4a","bitrate":32,"type_description":"压缩品质","url":"http://oen.cye.yymommy.com/f66db30f9c4296f7/1415675062/m4a_32_33/78/52/7869347cb0ec4d7e2570812d02425452.m4a?s=t","size":"0.67M","type":1}],"url_list":[{"duration":"02:50","format":"m4a","bitrate":96,"type_description":"标准品质","url":"http://b.ali.hotchanson.com/f66db30f9c4296f7/1415675062/m4a_96_33/78/52/7869347cb0ec4d7e2570812d02425452.m4a?s=t","size":"1.96M","type":2},{"duration":"02:51","format":"m4a","bitrate":32,"type_description":"压缩品质","url":"http://oen.cye.yymommy.com/f66db30f9c4296f7/1415675062/m4a_32_33/78/52/7869347cb0ec4d7e2570812d02425452.m4a?s=t","size":"0.67M","type":1}]},{"song_id":4947961,"singer_id":49606,"song_name":"Moonshadow","singer_name":"Music Themes","album_name":"Fur Elise","pick_count":0,"vip":0,"audition_list":[{"duration":"02:28","format":"mp3","bitrate":128,"type_description":"标准品质","url":"http://ws.cs.hotchanson.com/dbf224b96aa28270/1415675062/mp3_128_49/2b/33/2b8e82dfa3a6b66b61a20cbc5c866533.mp3?s=t","size":"2.27M","type":3},{"duration":"02:28","format":"m4a","bitrate":32,"type_description":"压缩品质","url":"http://oen.cye.yymommy.com/dbf224b96aa28270/1415675062/m4a_32_49/2b/33/2b8e82dfa3a6b66b61a20cbc5c866533.m4a?s=t","size":"0.58M","type":1}],"url_list":[{"duration":"02:28","format":"mp3","bitrate":128,"type_description":"标准品质","url":"http://ws.cs.hotchanson.com/dbf224b96aa28270/1415675062/mp3_128_49/2b/33/2b8e82dfa3a6b66b61a20cbc5c866533.mp3?s=t","size":"2.27M","type":3},{"duration":"02:28","format":"m4a","bitrate":32,"type_description":"压缩品质","url":"http://oen.cye.yymommy.com/dbf224b96aa28270/1415675062/m4a_32_49/2b/33/2b8e82dfa3a6b66b61a20cbc5c866533.m4a?s=t","size":"0.58M","type":1}]},{"song_id":4899584,"singer_id":11478,"song_name":"Moonshadow (As Made Famous By Cat Stevens)","singer_name":"Various Artists","album_name":"Adult Contemporary Hits","pick_count":0,"vip":0,"audition_list":[{"duration":"02:56","format":"mp3","bitrate":128,"type_description":"标准品质","url":"http://a.ali.dongting.com/ce0786086ebd18fb/1415675062/mp3_128_48/29/4f/29268c71b5347c8eb79fab35efe6b34f.mp3?s=t","size":"2.69M","type":3},{"duration":"02:56","format":"m4a","bitrate":32,"type_description":"压缩品质","url":"http://ws.cs.hotchanson.com/ce0786086ebd18fb/1415675062/m4a_32_48/29/4f/29268c71b5347c8eb79fab35efe6b34f.m4a?s=t","size":"0.69M","type":1}],"url_list":[{"duration":"02:56","format":"mp3","bitrate":128,"type_description":"标准品质","url":"http://a.ali.dongting.com/ce0786086ebd18fb/1415675062/mp3_128_48/29/4f/29268c71b5347c8eb79fab35efe6b34f.mp3?s=t","size":"2.69M","type":3},{"duration":"02:56","format":"m4a","bitrate":32,"type_description":"压缩品质","url":"http://ws.cs.hotchanson.com/ce0786086ebd18fb/1415675062/m4a_32_48/29/4f/29268c71b5347c8eb79fab35efe6b34f.m4a?s=t","size":"0.69M","type":1}]},{"song_id":4913346,"singer_id":11478,"song_name":"Moonshadow","singer_name":"Various Artists","album_name":"A Salute To Cat Stevens","pick_count":0,"vip":0,"audition_list":[{"duration":"02:56","format":"mp3","bitrate":128,"type_description":"标准品质","url":"http://jdlbqc.tgg.yymommy.com/74641fa323da838f/1415675062/mp3_128_49/53/a1/53deef77af92971460ae02ed9afc03a1.mp3?s=t","size":"2.69M","type":3},{"duration":"02:56","format":"m4a","bitrate":32,"type_description":"压缩品质","url":"http://b.ali.hotchanson.com/74641fa323da838f/1415675062/m4a_32_49/53/a1/53deef77af92971460ae02ed9afc03a1.m4a?s=t","size":"0.69M","type":1}],"url_list":[{"duration":"02:56","format":"mp3","bitrate":128,"type_description":"标准品质","url":"http://jdlbqc.tgg.yymommy.com/74641fa323da838f/1415675062/mp3_128_49/53/a1/53deef77af92971460ae02ed9afc03a1.mp3?s=t","size":"2.69M","type":3},{"duration":"02:56","format":"m4a","bitrate":32,"type_description":"压缩品质","url":"http://b.ali.hotchanson.com/74641fa323da838f/1415675062/m4a_32_49/53/a1/53deef77af92971460ae02ed9afc03a1.m4a?s=t","size":"0.69M","type":1}]}]}'''
    j = strToDict(x)
    print j["code"]
    z ='''{"code":1,"allPage":4,"count":23,"extra":{"all_page":4,"all_count":23,"v":"603"},"data":[{"song_id":11930538,"singer_id":183403,"song_name":"Moonshadow","singer_name":"Celia Pavey","album_name":"This Music","pick_count":4,"vip":0,"audition_list":[{"duration":"02:51","format":"m4a","bitrate":32,"type_description":"压缩品质","url":"http://ws.cs.hotchanson.com/8e377986ff57ee24/1415674809/m4a_32_119/7c/af/7c1f56fae6b935aadaffe7c7d78e2aaf.m4a?s=t","size":"0.68M","type":1},{"duration":"02:51","format":"m4a","bitrate":96,"type_description":"标准品质","url":"http://oen.cye.yymommy.com/8e377986ff57ee24/1415674809/m4a_96_119/7c/af/7c1f56fae6b935aadaffe7c7d78e2aaf.m4a?s=t","size":"1.97M","type":2},{"duration":"02:51","format":"mp3","bitrate":128,"type_description":"标准品质","url":"http://oen.cye.yymommy.com/8e377986ff57ee24/1415674809/mp3_128_119/7c/af/7c1f56fae6b935aadaffe7c7d78e2aaf.mp3?s=t","size":"2.61M","type":3}],"url_list":[{"duration":"02:51","format":"m4a","bitrate":32,"type_description":"压缩品质","url":"http://ws.cs.hotchanson.com/8e377986ff57ee24/1415674809/m4a_32_119/7c/af/7c1f56fae6b935aadaffe7c7d78e2aaf.m4a?s=t","size":"0.68M","type":1},{"duration":"02:51","format":"m4a","bitrate":96,"type_description":"标准品质","url":"http://oen.cye.yymommy.com/8e377986ff57ee24/1415674809/m4a_96_119/7c/af/7c1f56fae6b935aadaffe7c7d78e2aaf.m4a?s=t","size":"1.97M","type":2},{"duration":"02:51","format":"mp3","bitrate":128,"type_description":"标准品质","url":"http://oen.cye.yymommy.com/8e377986ff57ee24/1415674809/mp3_128_119/7c/af/7c1f56fae6b935aadaffe7c7d78e2aaf.mp3?s=t","size":"2.61M","type":3}]},{"song_id":243853,"singer_id":72912,"song_name":"Moonshadow","singer_name":"Mandy Moore","album_name":"Coverage","pick_count":17,"vip":0,"audition_list":[{"duration":"02:59","format":"m4a","bitrate":32,"type_description":"压缩品质","url":"http://oen.cye.yymommy.com/b97b163c05b81316/1415674809/m4a_32_2/26/2d/26c77336f71daa46dc50da6ccc64eb2d.m4a?s=t","size":"0.71M","type":1},{"duration":"02:59","format":"m4a","bitrate":96,"type_description":"标准品质","url":"http://oen.cye.yymommy.com/b97b163c05b81316/1415674809/m4a_96_2/26/2d/26c77336f71daa46dc50da6ccc64eb2d.m4a?s=t","size":"2.07M","type":2},{"duration":"02:59","format":"mp3","bitrate":128,"type_description":"标准品质","url":"http://oen.cye.yymommy.com/b97b163c05b81316/1415674809/mp3_128_2/26/2d/26c77336f71daa46dc50da6ccc64eb2d.mp3?s=t","size":"2.74M","type":3},{"duration":"02:59","format":"mp3","bitrate":192,"type_description":"高品质","url":"http://oen.cye.yymommy.com/4635a1267672c1e7/1415674809/mp3_190_2/cb/f6/cb2d9dc16d856b548a0ed87ec4569bf6.mp3?s=t","size":"4.11M","type":4},{"duration":"02:59","format":"mp3","bitrate":320,"type_description":"超高品质","url":"http://ws.cs.hotchanson.com/23f69711dacf12ad/1415674809/mp3_190_2/83/fa/83a1c9e76068da8808e6e76c263b05fa.mp3?s=t","size":"6.86M","type":5}],"url_list":[{"duration":"02:59","format":"m4a","bitrate":32,"type_description":"压缩品质","url":"http://oen.cye.yymommy.com/b97b163c05b81316/1415674809/m4a_32_2/26/2d/26c77336f71daa46dc50da6ccc64eb2d.m4a?s=t","size":"0.71M","type":1},{"duration":"02:59","format":"m4a","bitrate":96,"type_description":"标准品质","url":"http://oen.cye.yymommy.com/b97b163c05b81316/1415674809/m4a_96_2/26/2d/26c77336f71daa46dc50da6ccc64eb2d.m4a?s=t","size":"2.07M","type":2},{"duration":"02:59","format":"mp3","bitrate":128,"type_description":"标准品质","url":"http://oen.cye.yymommy.com/b97b163c05b81316/1415674809/mp3_128_2/26/2d/26c77336f71daa46dc50da6ccc64eb2d.mp3?s=t","size":"2.74M","type":3},{"duration":"02:59","format":"mp3","bitrate":192,"type_description":"高品质","url":"http://oen.cye.yymommy.com/4635a1267672c1e7/1415674809/mp3_190_2/cb/f6/cb2d9dc16d856b548a0ed87ec4569bf6.mp3?s=t","size":"4.11M","type":4},{"duration":"02:59","format":"mp3","bitrate":320,"type_description":"超高品质","url":"http://ws.cs.hotchanson.com/23f69711dacf12ad/1415674809/mp3_190_2/83/fa/83a1c9e76068da8808e6e76c263b05fa.mp3?s=t","size":"6.86M","type":5}]},{"song_id":1225886,"singer_id":12649,"song_name":"Moonshadow","singer_name":"Cat Stevens","album_name":"Icon","pick_count":6,"vip":0,"audition_list":[{"duration":"02:50","format":"m4a","bitrate":32,"type_description":"压缩品质","url":"http://ws.cs.hotchanson.com/6451a3a54059cc56/1415674809/m4a_32_12/41/7f/4139b95510c5bd25eba690381defb37f.m4a?s=t","size":"0.67M","type":1},{"duration":"02:50","format":"m4a","bitrate":96,"type_description":"标准品质","url":"http://a.ali.dongting.com/6451a3a54059cc56/1415674809/m4a_96_12/41/7f/4139b95510c5bd25eba690381defb37f.m4a?s=t","size":"1.95M","type":2},{"duration":"02:50","format":"mp3","bitrate":128,"type_description":"标准品质","url":"http://oen.cye.yymommy.com/6451a3a54059cc56/1415674809/mp3_128_12/41/7f/4139b95510c5bd25eba690381defb37f.mp3?s=t","size":"2.60M","type":3},{"duration":"02:50","format":"mp3","bitrate":192,"type_description":"高品质","url":"http://oen.cye.yymommy.com/381c7fafd3b0ee5b/1415674809/mp3_190_12/87/9b/876a122d86078e044948efd35f8b219b.mp3?s=t","size":"3.90M","type":4},{"duration":"02:50","format":"mp3","bitrate":320,"type_description":"超高品质","url":"http://oen.cye.yymommy.com/08653b2103b1b57f/1415674809/mp3_190_12/c8/51/c8a13287b34ec9991b9a84c1ae25c551.mp3?s=t","size":"6.50M","type":5}],"url_list":[{"duration":"02:50","format":"m4a","bitrate":32,"type_description":"压缩品质","url":"http://ws.cs.hotchanson.com/6451a3a54059cc56/1415674809/m4a_32_12/41/7f/4139b95510c5bd25eba690381defb37f.m4a?s=t","size":"0.67M","type":1},{"duration":"02:50","format":"m4a","bitrate":96,"type_description":"标准品质","url":"http://a.ali.dongting.com/6451a3a54059cc56/1415674809/m4a_96_12/41/7f/4139b95510c5bd25eba690381defb37f.m4a?s=t","size":"1.95M","type":2},{"duration":"02:50","format":"mp3","bitrate":128,"type_description":"标准品质","url":"http://oen.cye.yymommy.com/6451a3a54059cc56/1415674809/mp3_128_12/41/7f/4139b95510c5bd25eba690381defb37f.mp3?s=t","size":"2.60M","type":3},{"duration":"02:50","format":"mp3","bitrate":192,"type_description":"高品质","url":"http://oen.cye.yymommy.com/381c7fafd3b0ee5b/1415674809/mp3_190_12/87/9b/876a122d86078e044948efd35f8b219b.mp3?s=t","size":"3.90M","type":4},{"duration":"02:50","format":"mp3","bitrate":320,"type_description":"超高品质","url":"http://oen.cye.yymommy.com/08653b2103b1b57f/1415674809/mp3_190_12/c8/51/c8a13287b34ec9991b9a84c1ae25c551.mp3?s=t","size":"6.50M","type":5}],"ll_list":[{"duration":"02:50","format":"flac","bitrate":850,"type_description":"无损品质","url":"http://ws.cs.hotchanson.com/7cdddd9ef7eef2fe/1415674809/flac_190_12/16/b6/161cd13fc2272973bf5d677ea30fd3b6.flac?s=t","size":"17.28M"}]},{"song_id":27142367,"singer_id":12649,"song_name":"Moonshadow ","singer_name":"Cat Stevens","album_name":"Teaser And The Firecat","pick_count":0,"vip":0,"audition_list":[{"duration":"02:52","format":"m4a","bitrate":32,"type_description":"压缩品质","url":"http://oen.cye.yymommy.com/99f28381332a91b4/1415674809/m4a_32_271/7f/52/7fbd3f48b23fc638582eba17cacba552.m4a?s=t","size":"0.68M","type":1},{"duration":"02:52","format":"m4a","bitrate":96,"type_description":"标准品质","url":"http://a.ali.dongting.com/99f28381332a91b4/1415674809/m4a_96_271/7f/52/7fbd3f48b23fc638582eba17cacba552.m4a?s=t","size":"1.99M","type":2},{"duration":"02:52","format":"mp3","bitrate":128,"type_description":"标准品质","url":"http://oen.cye.yymommy.com/99f28381332a91b4/1415674809/mp3_128_271/7f/52/7fbd3f48b23fc638582eba17cacba552.mp3?s=t","size":"2.63M","type":3},{"duration":"02:52","format":"mp3","bitrate":192,"type_description":"高品质","url":"http://oen.cye.yymommy.com/c71462ae7337d071/1415674809/mp3_190_271/b1/79/b16626037db02497448c8c8304aec479.mp3?s=t","size":"3.95M","type":4},{"duration":"02:52","format":"mp3","bitrate":320,"type_description":"超高品质","url":"http://ws.cs.hotchanson.com/e05b68f44fc6b488/1415674809/mp3_190_271/56/e2/5642b0d941f2eb9032df972b393c63e2.mp3?s=t","size":"6.60M","type":5}],"url_list":[{"duration":"02:52","format":"m4a","bitrate":32,"type_description":"压缩品质","url":"http://oen.cye.yymommy.com/99f28381332a91b4/1415674809/m4a_32_271/7f/52/7fbd3f48b23fc638582eba17cacba552.m4a?s=t","size":"0.68M","type":1},{"duration":"02:52","format":"m4a","bitrate":96,"type_description":"标准品质","url":"http://a.ali.dongting.com/99f28381332a91b4/1415674809/m4a_96_271/7f/52/7fbd3f48b23fc638582eba17cacba552.m4a?s=t","size":"1.99M","type":2},{"duration":"02:52","format":"mp3","bitrate":128,"type_description":"标准品质","url":"http://oen.cye.yymommy.com/99f28381332a91b4/1415674809/mp3_128_271/7f/52/7fbd3f48b23fc638582eba17cacba552.mp3?s=t","size":"2.63M","type":3},{"duration":"02:52","format":"mp3","bitrate":192,"type_description":"高品质","url":"http://oen.cye.yymommy.com/c71462ae7337d071/1415674809/mp3_190_271/b1/79/b16626037db02497448c8c8304aec479.mp3?s=t","size":"3.95M","type":4},{"duration":"02:52","format":"mp3","bitrate":320,"type_description":"超高品质","url":"http://ws.cs.hotchanson.com/e05b68f44fc6b488/1415674809/mp3_190_271/56/e2/5642b0d941f2eb9032df972b393c63e2.mp3?s=t","size":"6.60M","type":5}]},{"song_id":837339,"singer_id":30902,"song_name":"Moonshadow","singer_name":"Ritsuko Okazaki","album_name":"Love   Life Private Works 1999-2001","pick_count":0,"vip":0,"audition_list":[{"duration":"06:29","format":"m4a","bitrate":32,"type_description":"压缩品质","url":"http://a.ali.dongting.com/c62bf194aeef7990/1415674809/m4a_32_8/4d/7a/4d6145a9bad632e781d25f42c603e47a.m4a?s=t","size":"1.53M","type":1},{"duration":"06:29","format":"m4a","bitrate":96,"type_description":"标准品质","url":"http://oen.cye.yymommy.com/c62bf194aeef7990/1415674809/m4a_96_8/4d/7a/4d6145a9bad632e781d25f42c603e47a.m4a?s=t","size":"4.49M","type":2},{"duration":"06:29","format":"mp3","bitrate":128,"type_description":"标准品质","url":"http://ws.cs.hotchanson.com/c62bf194aeef7990/1415674809/mp3_128_8/4d/7a/4d6145a9bad632e781d25f42c603e47a.mp3?s=t","size":"5.94M","type":3},{"duration":"06:29","format":"mp3","bitrate":192,"type_description":"高品质","url":"http://oen.cye.yymommy.com/b761a8e36e92c968/1415674809/mp3_190_8/32/8d/324dcff037692dba1fe75952d647258d.mp3?s=t","size":"8.91M","type":4},{"duration":"06:29","format":"mp3","bitrate":320,"type_description":"超高品质","url":"http://oen.cye.yymommy.com/cc37c52dfcd602a4/1415674809/mp3_190_8/98/05/98bca02e1a5b02602bf5a25467cc4b05.mp3?s=t","size":"14.86M","type":5}],"url_list":[{"duration":"06:29","format":"m4a","bitrate":32,"type_description":"压缩品质","url":"http://a.ali.dongting.com/c62bf194aeef7990/1415674809/m4a_32_8/4d/7a/4d6145a9bad632e781d25f42c603e47a.m4a?s=t","size":"1.53M","type":1},{"duration":"06:29","format":"m4a","bitrate":96,"type_description":"标准品质","url":"http://oen.cye.yymommy.com/c62bf194aeef7990/1415674809/m4a_96_8/4d/7a/4d6145a9bad632e781d25f42c603e47a.m4a?s=t","size":"4.49M","type":2},{"duration":"06:29","format":"mp3","bitrate":128,"type_description":"标准品质","url":"http://ws.cs.hotchanson.com/c62bf194aeef7990/1415674809/mp3_128_8/4d/7a/4d6145a9bad632e781d25f42c603e47a.mp3?s=t","size":"5.94M","type":3},{"duration":"06:29","format":"mp3","bitrate":192,"type_description":"高品质","url":"http://oen.cye.yymommy.com/b761a8e36e92c968/1415674809/mp3_190_8/32/8d/324dcff037692dba1fe75952d647258d.mp3?s=t","size":"8.91M","type":4},{"duration":"06:29","format":"mp3","bitrate":320,"type_description":"超高品质","url":"http://oen.cye.yymommy.com/cc37c52dfcd602a4/1415674809/mp3_190_8/98/05/98bca02e1a5b02602bf5a25467cc4b05.mp3?s=t","size":"14.86M","type":5}]}]}'''
    h = strToDict(z)
    print h["data"]
    print str(h)
    