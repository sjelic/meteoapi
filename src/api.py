"""Functions handling API endpoints."""

import database
import models


def getMeasurements():
    measurements = models.Measurement.query.all()
    measurements = map(lambda m: m.to_dict(), measurements)
    return list(measurements)


def createMeasurement(body):
    measurement = models.Measurement.from_dict(**body)
    database.db.session.add(measurement)
    database.db.session.commit()
    return measurement.to_dict()


def getMeasurementById(id):
    measurement = models.Measurement.query.filter_by(id=id).first()
    if measurement is None:
        return ("Measurement not found.", 404)
    return measurement.to_dict()


def updateMeasurementById(body, id):
    measurement = models.Measurement.query.filter_by(id=id).first()
    if measurement is None:
        return ("Measurement not found.", 404)
    measurement.lat = body["lat"]
    measurement.long = body["long"]
    measurement.lat = body["lat"]
    measurement.time = body["time"]
    measurement.variable = body["variable"]
    measurement.value = body["value"]
    database.db.session.commit()
    return 200


def removeMeasurementById(id):
    measurement = models.Measurement.query.filter_by(id=id).delete()
    if not measurement:
        return ("Measurement not found.", 404)
    database.db.session.commit()
    return 200