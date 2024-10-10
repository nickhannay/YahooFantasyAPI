import webbrowser
import pytest
import time
from dotenv import load_dotenv
import os 

from src.yfsAPI.auth import TokenManager, Token, AuthException

load_dotenv('../.env')

@pytest.fixture
def token_manager():
    return TokenManager(os.environ.get('client_id'), os.environ.get('client_secret'))


def test_auth_url(token_manager):
    url = token_manager.auth_url
    assert url == f'https://api.login.yahoo.com/oauth2/request_auth?client_id={client_id}&redirect_uri=oob&response_type=code&language=en-us'


def test_generate_valid_token(token_manager):
    webbrowser.open(token_manager.auth_url)
    auth_code = input('enter auth code: ')
    token = token_manager.generate_user_token('id1', auth_code)
    assert isinstance(token, Token)
    assert hasattr(token, 'access_token')
    assert hasattr(token, 'refresh_token')
    assert token.created_at <= time.time()


def test_generate_token_invalid_code(token_manager):
    with pytest.raises(AuthException):
        token_manager.generate_user_token('id2', 'invalid')


'''def test_refresh_token():
    token = Token('DaOE66qapgHPqH3zU2Yb.FOmhkp_JWxmkztIwfzQkEzvEBUhn0LyRY1aLw.BeR5bpkbJI_f.ZxfcqTd.QkH04V2i4ifUxT9PGLEsQlCgQh2gM4ZL7MKySd5yWzH1.EPOiF1G5upS767.Gsegs0__NSDeISfPObQ0OQTlEG.QxP8QA_1vYLjOGmNY6fs01WjoCoi0WEXhNs6AM1WECJuBNPkcse8FxgTUvW4OndaKNmOV2iYBkN6ILoqn8GXV8eC_Ix66_90WGxWzflSUgt8PFRL1KrTkDppHXJYmE7Eqboy7dwimy6R0GGZPee3IBANAQKz63t80BsVyTBnD8Q..oOd46FNWaP94pn8pgx6P5Rcz7TpJRIRKo1ovFH93d2bSzWvDtzFeOMdMVejfFk0Xq_ZfYZ92VTK7Q06fmFNIZlWT0060WOjUKxwOETNbSMdI1TWLjeERDsMmVWcL8Iy2TycoK_ZhncJQLzJAfL7qGMAQNlv4CPbX_AtGZrCtS_OyG233CbsMaRGrNwl0z18Rzgzp0VSIfsIBMtN4tSLh_r1JzQiHnheNqHh7FuSrH6_kVWZYve1Zz7_4Ln.xIMI6WhrJyYlG1eMa99BGTDboRiG2LlQxTUHTYiq3MsNJjOFzcSeMwDJr.cjanzthEnWECO4qjhaapP8nn95HOQuvl2nEvb8z4al9UBxizMtoiMxHH4HPze3Z.E.39oehjzG2Z4l2mGpmd280O2bkccJJwRty6zvnT0EV2hRJxF1FbAiBIysyz88I6OaSUgfDGyV1j11antNlEQkE3uBIkCIhyLpt1Ter2th8l0c78PB4YR0pzKDs5loonekb_14WkIqY4E0AQKnEGKO108ItLQOu1.qpgziH_gl_4PEDLmtHXY_f7uDHVoSV4zDdfjpepz1EQ4LiqJ8qRGehBWZXA2iHXGd4Tv8-',
                  'AI._9GbT396wSwmdSgd8nC8gW9Vs~001~ns65_c0fEKg8_rR3QRQ7g4.CWg--',
                  3600)
    print(f'old token : {token}')
    token_manager.refresh_token(token)
    print(token)'''