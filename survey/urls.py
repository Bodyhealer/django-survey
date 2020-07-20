# -*- coding: utf-8 -*-

from django.conf.urls import url

from survey.views import ConfirmView, IndexView, SurveyCompleted, SurveyDetail
from survey.views.survey_result import serve_result_csv

urlpatterns = [
    url(r"^$", IndexView.as_view(), name="survey-list"),
    url(r"^(?P<uuid>\d+)/", SurveyDetail.as_view(), name="survey-detail"),
    url(r"^csv/(?P<primary_key>\d+)/", serve_result_csv, name="survey-result"),
    url(r"^(?P<uuid>\d+)/completed/", SurveyCompleted.as_view(), name="survey-completed"),
    url(r"^(?P<uuid>\d+)-(?P<step>\d+)/", SurveyDetail.as_view(), name="survey-detail-step"),
    url(r"^confirm/(?P<uuid>\w+)/", ConfirmView.as_view(), name="survey-confirmation"),
]
