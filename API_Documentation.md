**This documentation is automatically generated.**

**Output schemas only represent `data` and not the full output; see output examples and the JSend specification.**

# /api/points/?

    Content-Type: application/json

## POST


**Input Schema**
```json
{
    "properties": {
        "lat_from": {
            "type": "number"
        },
        "lat_to": {
            "type": "number"
        },
        "long_to": {
            "type": "number"
        },
        "n_items": {
            "type": "number"
        },
        "time_from": {
            "type": "number"
        },
        "time_to": {
            "type": "number"
        }
    },
    "type": "object"
}
```


**Input Example**
```json
{
    "lat_from": -6.0303955,
    "lat_to": -6.0303955,
    "long_from": 106.8480445,
    "long_to": 107.0480445,
    "n_items": 900,
    "time_from": 0,
    "time_to": 24
}
```


**Output Schema**
```json
{
    "properties": {
        "points": {
            "items": {
                "type": "array"
            },
            "type": "array"
        }
    },
    "type": "object"
}
```


**Output Example**
```json
{
    "points": [
        [
            -6.2303955,
            106.8480445,
            2000
        ],
        [
            -6.2303955,
            106.8480445,
            2000
        ]
    ]
}
```


**Notes**

POST the required parameters
* `lat_from`: latitude from
* `long_from`: longitude from
* `lat_to`: latitude to
* `long_to`: longitude to
* `time_from`: time from
* `time_to`: time to
* `n_items`: how many max points returned


