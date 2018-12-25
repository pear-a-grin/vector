#!/usr/bin/env python3

"""Simple chat output.  Says somthing you type
"""

import anki_vector
from anki_vector.util import degrees
from random import randint
import string
import time

def playFromList(robot,key, n = 1):
    # Define various "emotion" lists
    anim_think = ['anim_eyecontact_lookloop_01_head_angle_20', 'anim_generic_look_up_idle_02', 'anim_freeplay_reacttoface_identified_03', 'anim_observing_around_subtle_01', 'anim_eyecontact_squint_01_head_angle_40', 'anim_hiking_lookaround_01', 'anim_reacttoface_unidentified_01_head_angle_40', 'anim_eyecontact_lookloop_02_head_angle_20']
    anim_happy = ['anim_fastbump_loop_01', 'anim_petting_lvl3_getout_02',  'anim_eyecontact_giggle_01_head_angle_-20', 'anim_fistbump_requesttwice_01', 'anim_reacttoblock_success_01', 'anim_onboarding_reacttoface_happy_01_head_angle_-20', 'anim_eyecontact_smile_01_head_angle_20', 'anim_reacttoface_unidentified_01', 'anim_reacttoface_unidentified_02', 'anim_pounce_lookloop_03', 'anim_reacttoface_unidentified_02_head_angle_20', 'anim_pounce_lookloop_02', 'anim_onboarding_reacttoface_happy_01', 'anim_spinner_tap_01', 'anim_feedback_goodrobot_02', 'anim_pounce_success_03',  'anim_pounce_success_01', 'anim_eyepose_happy', 'anim_reacttoblock_happydetermined_02']
    anim_sad = ['anim_keepaway_pounce_shake_02', 'anim_keepaway_hit_reaction_01', 'anim_reacttocliff_edge_04', 'anim_eyepose_sad', 'anim_dizzy_reaction_medium_02', 'anim_dizzy_reaction_soft_01', 'anim_eyepose_angry', 'anim_dizzy_shake_stop_01', 'anim_keepaway_pounce_quick_01', 'anim_handdetection_reaction_01', 'anim_feedback_badrobot_02', 'anim_eyepose_sad_up', 'anim_eyepose_sad_down01', 'anim_eyepose_sad_down', 'anim_eyepose_hurt']

    if key == "happy":
        anim_list = anim_happy
    elif key == "sad":
        anim_list = anim_sad
    elif key == "think":
        anim_list = anim_think
    else:
        anim_list = anim_happy

    for i in range(0,n):
        it = randint(0,len(anim_list)-1)
        print(f"Play {key} Animation #{it+1} of {len(anim_list)}: {anim_list[it]}")
        robot.anim.play_animation(anim_list[it])
        time.sleep(0.2)

def main():
    args = anki_vector.util.parse_command_args()

    
    with anki_vector.Robot(args.serial) as robot:
        robot.behavior.drive_off_charger()

        
        str = "nothing"
        while True:
            str = input("\nWhat should Vector say? \nthink \t= show thinking\nsad \t= do a sad thing\nhappy\t= do a happy thing\nr \t= turn right\nl \t= turn left\nexit \t= exit\n >>")
            if str == "exit":
                break
            elif str == "r":
                robot.anim.play_animation('anim_rtmotion_turn45right_01')
            elif str == "l":
                robot.anim.play_animation('anim_rtmotion_turn45left_01')
            elif str == "think":
                playFromList(robot,"think",3)
            elif str == "sad":
                playFromList(robot,"sad",2)
            elif str == "happy":
                playFromList(robot,"happy",5)
            else:          
                playFromList(robot,"happy")
                robot.say_text(str)
                playFromList(robot,"happy",3)
            
        
        robot.behavior.turn_in_place(degrees(360*1))
        robot.anim.play_animation('anim_reacttoblock_happydetermined_02')  


if __name__ == '__main__':
    main()
