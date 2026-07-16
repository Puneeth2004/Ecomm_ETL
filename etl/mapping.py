TABLE_MAPPING = {

    "orders": {
        "drop_columns": [
            "payment_id",
            "shipping_id"
        ]
    },

    "inventory": {
        "type_conversion": {
            "reorder_level": "Int64"
        }
    }

}


PRELOAD_SCHEMA = {

    "categories": [
        "category_id",
        "category_name"
    ],

    "customers": [
        "customer_id",
        "first_name",
        "last_name",
        "email",
        "phone",
        "gender",
        "city",
        "state",
        "country",
        "signup_date"
    ],

    "products": [
        "product_id",
        "product_name",
        "category_id",
        "brand",
        "cost_price",
        "selling_price",
        "stock_quantity"
    ],

    "inventory": [
        "inventory_id",
        "product_id",
        "warehouse",
        "stock_quantity",
        "reorder_level",
        "last_restock_date"
    ],

    "orders": [
        "order_id",
        "customer_id",
        "order_date",
        "status"
    ],

    "payments": [
        "payment_id",
        "order_id",
        "payment_method",
        "amount",
        "status",
        "payment_date"
    ],

    "shipping": [
        "shipping_id",
        "order_id",
        "carrier",
        "shipping_date",
        "delivery_date",
        "shipping_cost"
    ],

    "returns": [
        "return_id",
        "order_id",
        "return_reason",
        "return_date",
        "refund_amount"
    ],

    "reviews": [
        "review_id",
        "customer_id",
        "product_id",
        "order_id",
        "rating",
        "review_text",
        "review_date"
    ],

    "order_items": [
        "order_item_id",
        "order_id",
        "product_id",
        "quantity",
        "unit_price",
        "discount",
        "line_total"
    ]

}