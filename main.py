import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation, Donor

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('all'))

@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)

@app.route('/donations/<name>')
def single_donor(name):
    donations = Donation.select().join(Donor).where(Donor.name == name)
    #donations = Donation.select().where(Donation.donor.name == 'Bob')

    return render_template('individual_donations.jinja2', donations=donations, name=name)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
