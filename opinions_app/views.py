from random import randrange

from flask import abort, flash, redirect, render_template, url_for

from . import app, db
from .forms import OpinionForm
from .models import Opinion


def random_opinion():
    quntity = Opinion.query.count()
    if quntity:
        offset_value = randrange(quntity)
        opinion = Opinion.query.offset(offset_value).first()
        return opinion

@app.route('/')
def index_view():
    opinion = random_opinion()
    quntity = Opinion.query.count()
    if not quntity:
        abort(500)
    return render_template('opinion.html', opinion=opinion)

@app.route('/add', methods=['GET', 'POST'])
def add_opinion_view():
    form = OpinionForm()
    if form.validate_on_submit():
        text = form.text.data
        if Opinion.query.filter_by(text=text).first():
            flash('This opininon already exists')
            return render_template('add_opinion.html', form=form)
        opinion = Opinion(
            title=form.title.data,
            text=form.text.data,
            source=form.source.data
        )
        db.session.add(opinion)
        db.session.commit()
        return redirect(url_for('opinion_view', id=opinion.id))
    return render_template('add_opinion.html', form=form)

@app.route('/opinions/<int:id>')
def opinion_view(id):
    return render_template(
        'opinion.html',
        opinion=Opinion.query.get_or_404(id)
    )
