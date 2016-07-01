# coding: utf-8
PHRASE_PARAM_TYPE_INT = 'integer'
PHRASE_PARAM_TYPE_TIME = 'time'
PHRASE_PARAM_TYPE_DATE = 'date'
PHRASE_PARAM_TYPE_DATETIME = 'date_time'
PHRASE_PARAM_TYPE_REGEXP = 'regexp'
PHRASE_PARAM_TYPE_CHOICES = (
    (PHRASE_PARAM_TYPE_INT, 'число'),
    (PHRASE_PARAM_TYPE_TIME, 'время'),
    (PHRASE_PARAM_TYPE_DATE, 'дата'),
    (PHRASE_PARAM_TYPE_DATETIME, 'дата и время'),
    (PHRASE_PARAM_TYPE_REGEXP, 'регулярное выражение'),
)