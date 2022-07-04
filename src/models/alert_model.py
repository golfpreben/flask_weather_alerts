from sqlalchemy import Column, Text, Integer

from src.models.base_model import BaseModel, db


class AlertModel(BaseModel, db.Model):
    """ Model describing an alert """

    temperature_below_threshold_celsius = Column(Integer)
    alert_destination = Column(Text)