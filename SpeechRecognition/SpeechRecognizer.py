# This code is from test_microphone.py form vosk
# TODO : 1. Make this file to print the output properly  like live changing line word by word. 2. From the main vosk folder remove the unessecary folders and files which are for other language projects.

import argparse
import json
import os
import queue
import sounddevice as sd
import vosk
import sys

# import main
from AI_Bot import AI_brain
from TextToSpeech import TTS

q = queue.Queue()

def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text

def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument(
    '-l', '--list-devices', action='store_true',
    help='show list of audio devices and exit')
args, remaining = parser.parse_known_args()
if args.list_devices:
    print(sd.query_devices())
    parser.exit(0)
parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[parser])
parser.add_argument(
    '-f', '--filename', type=str, metavar='FILENAME',
    help='audio file to store recording to')
parser.add_argument(
    '-m', '--model', type=str, metavar='MODEL_PATH',
    help='Path to the model')
parser.add_argument(
    '-d', '--device', type=int_or_str,
    help='input device (numeric ID or substring)')
parser.add_argument(
    '-r', '--samplerate', type=int, help='sampling rate')
args = parser.parse_args(remaining)

def detect():
    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            result = rec.Result()
            result = json.loads(result)
            text = result['text']
            # main.getVoice(text)
            print(text)
            if str(text) == "kill" or str(text) == "kim":
                TTS.speak("Bye Sir")
                break
            AI_brain.chat(text)
            # remember.write(text + '\n')     # only use this whenever you need it for storing otherwise it simply makes the program sloower.
        else:
            # presult=rec.PartialResult()
            # presult=json.loads(presult)
            # ptext=presult['partial']
            # print(ptext)
            pass
        # if dump_fn is not None:
        #     dump_fn.write(data)
        # remember.write(rec.Result() + '\n')    # dont do this it is degrading the performance.


def run():
    try:
        # remember = open('output.txt', 'a')
        if args.model is None:
            args.model = "SpeechRecognition\model"
        if not os.path.exists(args.model):
            print ("Please download a model for your language from https://alphacephei.com/vosk/models")
            print ("and unpack as 'model' in the current folder.")
            parser.exit(0)
        if args.samplerate is None:
            device_info = sd.query_devices(args.device, 'input')
            # soundfile expects an int, sounddevice provides a float:
            args.samplerate = int(device_info['default_samplerate'])

        model = vosk.Model(args.model)

        if args.filename:
            dump_fn = open(args.filename, "wb")
        else:
            dump_fn = None

        with sd.RawInputStream(samplerate=args.samplerate, blocksize = 8000, device=args.device, dtype='int16',
                                channels=1, callback=callback):
                print('#' * 80)
                print('Press Ctrl+C to stop the recording')
                print('#' * 80)

                global rec
                rec = vosk.KaldiRecognizer(model, args.samplerate)
                detect()


    except KeyboardInterrupt:
        print('\n ------------------------- Done -------------------------')
        # remember.close()
        parser.exit(0)
    except Exception as e:
        parser.exit(type(e).__name__ + ': ' + str(e))


# run()
