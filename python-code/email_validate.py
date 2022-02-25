#  python -m pip install -U email-validate
from email_validate import validate, validate_or_fail
validate(
    email_address='hello@00.pe',
    check_format=True,
    check_blacklist=True,
    check_dns=True,
    dns_timeout=10,
    check_smtp=False,
    smtp_debug=False)
# False

validate(
    email_address='rashidovabdurakhmon@gmail.com',
    check_format=True,
    check_blacklist=True,
    check_dns=True,
    dns_timeout=10,
    check_smtp=False,
    smtp_debug=False)
# True


# Параметры:

# email_address: адрес электронной почты для проверки.
# check_format: проверяет правильность структуры адреса электронной почты. По умолчанию True.
# check_blacklist: проверяет электронную почту по черному списку доменов, загруженных из временных данных электронной почты DadouData (ежедневное обновление!!!); По умолчанию True.
# check_dns: проверяет mx-записи DNS, по умолчанию True.
# dns_timeout: секунды до тайм-аута DNS, по умолчанию 10 секунд.
# check_smtp: проверяет, действительно ли существует электронная почта, инициировав SMTP-диалог, по умолчанию True.
# smtp_timeout: секунды до истечения времени ожидания SMTP, по умолчанию 10 секунд
# smtp_helo_host: имя хоста для использования в SMTP HELO/EHLO; если установлено значение None (по умолчанию), то используется полное доменное имя локального хоста.
# smtp_from_address: адрес электронной почты, используемый отправителем в SMTP-опросе. Если установлено значение None (по умолчанию), то аргумент email_address также используется в качестве отправителя.
# smtp_debug: активирует отладочный вывод smtplib, который всегда направляется на stderr, по умолчанию False.