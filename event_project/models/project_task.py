# -*- coding: utf-8 -*-
# Python source code encoding : https://www.python.org/dev/peps/pep-0263/
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################
from openerp import models, fields


class ProjectTask(models.Model):
    _inherit = 'project.task'

    event = fields.Many2one(comodel_name='event.event',
                            inverse_name='tasks', string='Event')
