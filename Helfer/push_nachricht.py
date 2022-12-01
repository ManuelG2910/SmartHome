from pushnotifier import PushNotifier as pn


class push_nachricht:

    #pn = pn.PushNotifier('username', 'password', 'package_name', 'api_key')
    pn = pn.PushNotifier('dhbwprojektsmarthome', 'Smarthome22', 'pushNotifier', '8E7TV75BBV46B5HB6TE7T52VBETFBFBBTTFBETFBFB')

    pn.login('Smarthome22')
    {
        'username': 'dhbwprojektsmarthome',
        'avatar': 'https://gravatar.com/avatar/faedc831a6c911569d1830cfd2a89af9?s=128&d=wavatar&r=x',
        'app_token': '8E7TV75BBV46B5HB6TE7T52VBETFBFBBTTFBETFBFB',
    }

    pn.send_text('text', devices=['ID1', 'ID2'], silent=True)



