# -*- coding: utf-8 -*-
# Python source code encoding : https://www.python.org/dev/peps/pep-0263/
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################

from openerp import models, fields, api


class EventEvent(models.Model):
    _inherit = 'event.event'

    project_template = fields.Many2one(
        comodel_name='project.project', string='Template project',
        domain="[('state', '=', 'template')]")
    project = fields.Many2one(
        comodel_name='project.project', string='Related project',
        readonly=True)
    tasks = fields.One2many(
        comodel_name='project.task', related='project.task_ids',
        string='Tasks')
    count_tasks = fields.Integer(string='Task number', compute='_count_tasks')

    @api.one
    @api.depends('tasks')
    def _count_tasks(self):
        self.count_tasks = len(self.tasks)

    def project_template_duplicate(self):
        if self.project_template and not self.project:
            assert len(self) >= 0 and len(self) <= 1, "Expected singleton"
            result = self.project_template.duplicate_template()
            self.project = result['res_id']
            name = self.name
            self.project.write({'name': name,
                                'date_start': self.date_begin,
                                'date': self.date_begin,
                                'calculation_type': 'date_end'})
            self.project.project_recalculate()
            return True
        return False

    def project_data_update(self, vals):
        map_vals = {}
        recalculate = False
        if self.project:
            if vals.get('name'):
                map_vals['name'] = self.name
            if vals.get('date_begin'):
                map_vals['date_start'] = self.date_begin
                map_vals['date'] = self.date_begin
                recalculate = True
            if map_vals:
                self.project.write(map_vals)
                if recalculate:
                    self.project.project_recalculate()
        return True

    @api.model
    def create(self, vals):
        event = super(EventEvent, self).create(vals)
        event.project_template_duplicate()
        return event

    @api.multi
    def write(self, vals):
        super(EventEvent, self).write(vals)
        if not self.project_template_duplicate():
            self.project_data_update(vals)
        return True
