#
#    This file is part of Scalable COncurrent Operations in Python (SCOOP).
#
#    SCOOP is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of
#    the License, or (at your option) any later version.
#
#    SCOOP is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with SCOOP. If not, see <http://www.gnu.org/licenses/>.
#

# -t : Enforce a shell to be created to hold the remote comand.
#      This allows the kill of the remote command on ssh's termination
# -x : Disable X11 redirection.
# -n : Attach stdin to /dev/null .
BASE_SSH = ['ssh', '-t', '-x', '-n', '-oStrictHostKeyChecking=no']
