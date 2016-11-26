import tornado
from tornado_json.requesthandlers import APIHandler
from tornado_json import schema

class Points(APIHandler):

    @schema.validate(
        input_schema={
            "type": "object",
            "properties": {
                "lat_from": {"type": "number"},
                "long_to": {"type": "number"},
                "lat_to": {"type": "number"},
                "long_to": {"type": "number"},
                "time_from": {"type": "number"},
                "time_to": {"type": "number"},
                "n_items": {"type": "number"},
            }
        },
        input_example={
            "lat_from": -6.0303955,
            "long_from": 106.8480445,
            "lat_to": -6.0303955,
            "long_to": 107.0480445,
            "time_from": 0,
            "time_to": 24,
            "n_items": 900
            },
        output_schema={
            "type": "object",
            "properties": {
                "points": {"type": "array", "items": {"type": "array"}}
            }
        },
        output_example={
            "points": [[-6.2303955, 106.8480445, 2000],[-6.2303955, 106.8480445, 2000]]
        },
    )

    def post(self):
        """
        POST the required parameters
        * `lat_from`: latitude from
        * `long_from`: longitude from
        * `lat_to`: latitude to
        * `long_to`: longitude to
        * `time_from`: time from
        * `time_to`: time to
        * `n_items`: how many max points returned
        """
        tornado.log.enable_pretty_logging()
        return {
            # "points": [[self.body["lat_from"]]]
            "points": [[-6.2303955, 106.8480445, 2000],[-6.2303955, 106.8480445, 2000]]
        }

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Server", "GoViz v0.1.0.0")
        self.set_header("Access-Control-Allow-Headers", 'DNT,X-CustomHeader,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type')
        self.set_header('Access-Control-Allow-Methods', 'POST, OPTIONS')

    def options(self):
        self.set_status(204)
        self.clear_header('Content-Type')
        self.finish()
