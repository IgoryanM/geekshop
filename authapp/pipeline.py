import datetime

import requests
from social_core.exceptions import AuthForbidden

from authapp.models import ShopUserProfile


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return
    api_url = f"https://api.vk.com/method/users.get?fields=bdate,sex,about,city,photo_max_orig&access_token={response['access_token']}&v=5.92"

    resp = requests.get(api_url)
    if resp.status_code != 200:
        return
    data = resp.json()['response'][0]
    print(data)
    if data['sex']:
        if data['sex'] == 1:
            user.shopuserprofile.gender = ShopUserProfile.FEMALE
        elif data['sex'] == 2:
            user.shopuserprofile.gender = ShopUserProfile.MALE

    if data['about']:
        user.shopuserprofile.about_me = data['about']

    if data['bdate']:
        bdate = datetime.datetime.strptime(data['bdate'], '%d.%m.%Y').date()
        age = datetime.datetime.now().date().year - bdate.year
        if age < 18:
            user.delete()
            raise AuthForbidden('social_core.backends.vk.VKOAuth2')

    if data['photo_max_orig']:
        photo = requests.get(data['photo_max_orig'])
        if photo.status_code == 200:
            photoname = f'/users_avatars/{user.pk}.jpg'
            with open(f'media/{photoname}', 'wb') as avatar:
                avatar.write(photo.content)
                user.avatar = photoname

    user.save()
