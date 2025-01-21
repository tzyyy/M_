# coding=utf8


def generate_random_str(length=8):
    """
    生成随机字符串
    @param length: 字符串长度
    @return:
    """
    from django.utils.crypto import get_random_string

    if not length:
        length = 8

    return get_random_string(length)


def generate_md5_Str(src_str):
    """
    字符串生成md5
    @param src_str:
    @return:
    """
    import hashlib
    src_str = str(src_str)
    return hashlib.md5(src_str.encode('utf-8')).hexdigest()


def generate_user_password(user_password):
    """
    生成用户名登录用的密码
    @param user_password:
    @return:
    """
    if not user_password:
        return ""

    salt_str = generate_random_str(length=8)
    # md5字符串
    md5_str = generate_md5_Str(f'{user_password}.{salt_str}')

    return f'{md5_str}.{salt_str}'


def verify_user_password(user_password, db_password):
    """
    校验用户密码
    @param user_password: 用户原始密码
    @param db_password: db中的密码
    @return:
    """
    salt_str = db_password.split('.')[1]
    # md5字符串
    md5_str = generate_md5_Str(f'{user_password}.{salt_str}')

    return f'{md5_str}.{salt_str}' == db_password
