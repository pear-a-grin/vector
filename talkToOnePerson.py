#!/usr/bin/env python3

# Copyright (c) 2018 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Say something and spin
"""

import anki_vector
from anki_vector.util import degrees


def main():
    args = anki_vector.util.parse_command_args()

    with anki_vector.Robot(args.serial) as robot:
        robot.behavior.drive_off_charger()
        
        person_name = input("What name do you want to use?  ")
        robot.behavior.drive_off_charger()
        robot.anim.play_animation('anim_feedback_goodrobot_02')
        robot.say_text(f"{person_name}.  {person_name}. . . Hi, {person_name}.")
        robot.anim.play_animation('anim_referencing_giggle_01')
        #robot.say_text("My name is Vector. with a V. ")
        robot.anim.play_animation('anim_spinner_tap_01')
        robot.say_text(f"I am a robot.  . Are you a robot like me {person_name}?")
        robot.anim.play_animation('anim_reacttoblock_happydetermined_02')
        robot.say_text(f"I love you {person_name}.")
        robot.anim.play_animation('anim_feedback_goodrobot_02')
        
    robot.anim.play_animation('anim_spinner_tap_01') 
    robot.anim.play_animation('anim_reacttoblock_happydetermined_02')  


if __name__ == '__main__':
    main()
