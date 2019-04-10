
#Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey_Mini/LaunchkeyMini.py
#from Launchkey.Launchkey import Launchkey, LaunchkeyControlFactory, make_button
from __future__ import with_statement 

import sys
import Live

from _Framework.InputControlElement import *
from _Framework.ControlSurface import ControlSurface
from _Framework.TransportComponent import TransportComponent
from _Framework.MixerComponent import MixerComponent
from _Framework.DeviceComponent import DeviceComponent
from _Framework.EncoderElement import EncoderElement
from _Framework.SliderElement import SliderElement
from _Framework.ButtonElement import ButtonElement

from DeviceNavComponent import DeviceNavComponent
from Launchkey.Launchkey import make_encoder


CHANNEL = 15

# copied from InputControlElement for debugging
MIDI_NOTE_TYPE = 0
MIDI_CC_TYPE = 1

DEVICE_KNOBS = [7,8,9,10,11,12,13,14]
DEVICE_ON = 15
DEVICE_LOCK = 16 
DEVICE_BANK_UP = 17
DEVICE_BANK_DOWN = 18
DEVICE_NEXT = 19
DEVICE_PREV = 20

TAP_TEMPO = 108
METRONOME = 109
TEMPO_KNOB = 110


FADERS = [49,50,51,52,53,54,55,56] # these are the midi control values for the knobs of the LK Mini 
MASTER_FADER = 47

REVERSE = 112   
FORWARD = 113
STOP = 114
PLAY = 115
REC  = 116

PADS = [[40, 41, 42, 43, 48, 49, 50, 51], 
        [36, 37, 38, 39, 44, 45, 46, 47]] # this is the midi note values of the grid of 16 buttons arranged by row/column  
SCENES = [108, 109] # midi controller values for the two scene launch buttons 

class X_stationMG(ControlSurface):
    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        #super(LaunchkeyMini, self).__init__(c_instance, control_factory=LaunchkeyMiniControlFactory(), identity_response=(240, 126, 127, 6, 2, 0, 32, 41, 53, 0, 0))
        self._suppress_send_midi = True
        self._suppress_session_highlight = True
        self._control_is_with_automap = False

        self._suggested_input_port = 'LK Mini MIDI'
        self._suggested_output_port = 'LK Mini MIDI'
        with self.component_guard():
            self._MG_setup()

    def _MG_setup(self): 
        mixer = MixerComponent(8)
        mixer.set_track_offset(0) #Sets start point for mixer strip (offset from left)
        transport = TransportComponent()
        mixer.set_track_offset(0)
        

        for i in xrange(len(FADERS)): #set the functions of the knobs
            volume_knob = SliderElement(MIDI_CC_TYPE, CHANNEL, FADERS[i])
            # pan_knob = SliderElement(MIDI_CC_TYPE, 1, KNOBS[i])

            # send_a = SliderElement(MIDI_CC_TYPE, 2, KNOBS[i])
            # send_b = SliderElement(MIDI_CC_TYPE, 3, KNOBS[i])
            # send_c = SliderElement(MIDI_CC_TYPE, 4, KNOBS[i])
            # send_d = SliderElement(MIDI_CC_TYPE, 5, KNOBS[i])
            # send_e = SliderElement(MIDI_CC_TYPE, 6, KNOBS[i])
            # send_f = SliderElement(MIDI_CC_TYPE, 7, KNOBS[i])

            mixer.channel_strip(i).set_volume_control(volume_knob)
            # mixer.channel_strip(i).set_pan_control(pan_knob)
            # mixer.channel_strip(i).set_send_controls([send_a,
            #                                         send_b,
            #                                         send_c, 
            #                                         send_d,
            #                                         send_e,
            #                                         send_f])

          # scenes are locked to channel 14
        transport.set_overdub_button(ButtonElement(False, MIDI_CC_TYPE, CHANNEL, REC))
        transport.set_stop_button(ButtonElement(False, MIDI_CC_TYPE, CHANNEL, STOP))                 
        transport.set_play_button(ButtonElement(False, MIDI_CC_TYPE, CHANNEL, PLAY))
          # code left above so you cant replace either button with a play button
        self._device = DeviceComponent()
        device_param_controls = []
        for i in xrange(len(DEVICE_KNOBS)):
            device_param_controls.append(SliderElement(MIDI_CC_TYPE, CHANNEL, DEVICE_KNOBS[i]))
        self._device.set_parameter_controls(device_param_controls)
        self._device.set_on_off_button(ButtonElement(True, MIDI_CC_TYPE, CHANNEL, DEVICE_ON))
        # self._device.set_lock_button(ButtonElement(True, MIDI_CC_TYPE, CHANNEL_FX, DEVICE_LOCK))
        up_bank_button = ButtonElement(True, MIDI_CC_TYPE, CHANNEL, DEVICE_BANK_UP)
        down_bank_button = ButtonElement(True, MIDI_CC_TYPE, CHANNEL, DEVICE_BANK_DOWN)
        self.set_device_component(self._device)
        self._device_nav = DeviceNavComponent()
        self._device_nav.set_device_nav_buttons(ButtonElement(True, MIDI_CC_TYPE, CHANNEL, DEVICE_PREV),ButtonElement(True, MIDI_CC_TYPE, CHANNEL, DEVICE_NEXT))
        self._device.set_bank_prev_button(down_bank_button)
        self._device.set_bank_next_button(up_bank_button)


    def disconnect(self):
        ControlSurface.disconnect(self)
                                                                              
                                                                                                           
                                                                                                           
                                                                                                           
                                                                                                           
                                                                                                           
                                                                                                           
                                                                                                           
