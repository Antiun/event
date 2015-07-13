# -*- coding: utf-8 -*-
# Python source code encoding : https://www.python.org/dev/peps/pep-0263/
##############################################################################
#
#    OpenERP, Odoo Source Management Solution
#    Copyright (c) 2014 Serv. Tecnol. Avanzados (http://www.serviciosbaeza.com)
#                       Pedro M. Baeza <pedro.baeza@serviciosbaeza.com>
#    Copyright (c) 2015 Antiun Ingeniería S.L. (http://www.antiun.com)
#                       Endika Iglesias <endikaig@antiun.com>
#                       Antonio Espinosa <antonioea@antiun.com>
#                       Javier Iniesta <javieria@antiun.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Event project",
    "version": "1.0",
    "author": "Antiun Ingeniería S.L., "
              "Serv. Tecnol. Avanzados - Pedro M. Baeza, ",
    "website": "http://www.antiun.com",
    "license": "AGPL-3",
    "category": "Event Management",
    "depends": [
        'base',
        'event',
        'project_recalculate'
    ],
    'data': [
        "views/project_task_view.xml",
        "views/event_event_view.xml",
    ],
    "installable": True,
}
