# TODO IMPLANTAR
from flask import Blueprint, request, jsonify, current_app, render_template
from db.models import Product
from db.serialize import ProductSchema
import json

product = Blueprint('product',__name__)
