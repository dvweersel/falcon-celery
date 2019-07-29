from app.data.dummy import get_data
from app.model.model import Regressor
import json


class Fit:
    @staticmethod
    def on_post(req, resp):
        """
            Fits a regressor with degree d
        """
        x, y = get_data()

        d = int(req.media.get('d'))

        model = Regressor(degree=d)
        score = model.fit(x, y)
        model.save()

        resp.body = json.dumps({'success': "Model artifact written in JSON format",
                                'components': model.get_components(),
                                'score': model.mse})

    @staticmethod
    def on_get(req, resp):
        """
            Returns the fitted regressor
        """
        model = Regressor()
        try:
            model.load()

            if model.is_fitted:
                resp.body = json.dumps({'components': model.get_components(),
                                        'score': model.mse})
            else:
                resp.body = json.dumps({'error': 'Model not fitted'})
        except FileNotFoundError as e:
            resp.body = json.dumps({'error': 'Model not fitted'})


class Predict:

    @staticmethod
    def on_post(req, resp):
        try:
            model = Regressor()
            x = req.media.get('x')
            if isinstance(x, list):
                model.load()
                resp.body = json.dumps(model.predict(x).tolist())  # predict on the same x (!)
            else:
                resp.body = json.dumps({'error': 'TypeError: Input should be a list'})
        except FileNotFoundError:
            resp.body = json.dumps({'error': "Model not trained yet"})

    @staticmethod
    def on_get(req, resp):
        try:
            model = Regressor()
            model.load()
            x = req.media.get('x')

            resp.body = json.dumps(model.predict(x).tolist())  # predict on the same x (!)
        except FileNotFoundError:
            resp.body = json.dumps({'error': "Model not trained yet"})
        except AttributeError:
            resp.body = json.dumps({'error': "No input given"})

