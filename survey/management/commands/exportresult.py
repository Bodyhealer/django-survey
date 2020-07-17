# -*- coding: utf-8 -*-

import logging
import sys

from django.utils import translation

from survey.exporter.csv import Survey2Csv
from survey.exporter.tex.configuration import Configuration
from survey.management.survey_command import SurveyCommand

LOGGER = logging.getLogger(__name__)


class Command(SurveyCommand):

    """
        See the "help" var.
    """

    help = """This command permit to export all survey in the database as csv and tex."""

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument("--configuration-file", "-c", type=str, help="Path to the tex configuration file.")
        parser.add_argument(
            "--force",
            "-f",
            action="store_true",
            help="Force the generation, even if the file already exists. Default is False.",
        )
        parser.add_argument("--csv", action="store_true", help="Export as csv. Default is False.")
        parser.add_argument(
            "--language", help="Permit to change the language used for generation (default is defined in the settings)."
        )

    def check_nothing_at_all(self, options):
        SurveyCommand.check_nothing_at_all(options)
        if not options["csv"]:
            sys.exit("Nothing to do : add option --csv.")

    def handle(self, *args, **options):
        super(Command, self).handle(*args, **options)
        translation.activate(options.get("language"))
        for survey in self.surveys:
            LOGGER.info("Generating results for '%s'", survey)
            exporters = []
            if options["csv"]:
                exporters.append(Survey2Csv(survey))
            for exporter in exporters:
                if options["force"] or exporter.need_update():
                    exporter.generate_file()
                else:
                    LOGGER.warning(
                        "\t- %s's %s were already generated use the --force (-f) option to generate anyway.",
                        survey,
                        exporter.mime_type,
                    )
