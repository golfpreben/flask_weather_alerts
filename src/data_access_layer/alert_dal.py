from typing import List

from flask_restx import abort

from src.models.alert_model import AlertModel
from sqlalchemy.exc import NoResultFound

from src.models.base_model import db


class AlertDAL:

    def __init__(self):
        self.db = db

    def get_alerts(self) -> List[AlertModel]:
        """ Returns a list of all alerts """

        try:
            alerts = AlertModel.query.all()
            return alerts
        except NoResultFound as e:
            abort(404)
        except Exception as e:
            abort(500)

    def create_alert(self, alert_model_obj: AlertModel) -> AlertModel:
        """ Create an alert """
        try:
            self.db.session.add(alert_model_obj)
            self.db.session.commit()
            return alert_model_obj
        except Exception as e:
            abort(500, "Failed to create alert")
