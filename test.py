import hashlib




def register(secret):
    md5 = hashlib.md5('6a9a5ba51e2d014bd678f866ee467fd6'.encode(encoding='UTF-8'))
    md5.update(secret.encode(encoding='UTF-8'))
    local_secret = md5.hexdigest()
    print(local_secret)

s = '__jdc=122270672;__jdb=122270672.4.1611845408370462135656|1.1611845408;__jda=122270672.1611845408370462135656.1611845408.1611845408.1611845408.1;shshshsID=39053d45fa141bfafa9a2afe4a8ec75d_1_1611845412338;shshshfpb=eWZ3lPnD%2FKV7YOQ8wOmK%2F8w%3D%3D;shshshfp=7c83eafa775d76180395dc2508ac98dc;TrackID=1KtO5cXGTtuHgmU7Yw2GbuIfzhYdDtpHntCgn6IFED619Q0Q6vJKorH7_7khcGY9PKMXuK-TCBCVrmSCUVvLfXSbDwHHc-CMaPb6GWlijLokyVVY0dj7VOF8KWKzY6nGZ;unick=%E4%B8%9C%E4%BA%AC%E4%BC%9A%E5%91%98VIP;_pst=3248884568;_tp=Cm4nrHC1g4CVdkf5st5g%2FQ%3D%3D;areaId=1;shshshfpa=f82aecea-6ce1-2e83-ebed-35a26e39064a-1611845412;ceshi3.com=201;ipLoc-djd=1-0-0-0;pinId=QN1q7VZjGgbBJqKyyYWCow;thor=77F3250B9693C119CC90EB6BB73E1B2EF73BC162132B7746276685F49257363082790BFFD88D7FE8FA61BBFC1753C1DFA60A3CE0BD94E2C166A0352C8E207190C61DED3C3C8404C2AE245CB8C44670247C272E4BE39E60E7C012438FC6CD3477B34ADE5919F092C74A9DEF5C76C62960613BD2988A326630AF937D50B358DE3C4B19711076C1DB524B2CDAC4E15860AC;__jdu=1611845408370462135656;3AB9D23F7A4B3C9B=A3O455IQ4JLN4EUPIZTI4DZKMSDWCPY4VNJHXVAOU4NLKWSGNO6NDN53TO7RRPVDJVTELS4ZPMWANTKAULVGL7A3B4;pin=3248884568;__jdv=122270672|direct|-|none|-|1611845408371;'

if __name__ == '__main__':
    register('a296490e49f81b6e4ccece9bcb6f6a7b')
