from neorec import *
import numpy as np


# example of obtaining EEG data
def get_eeg_data():
    amp = NeoRec()

    amp.open()
    amp.setup(
        mode=NR_MODE_DATA,
        rate=NR_RATE_125HZ,
        range=NR_RANGE_mV300
    )
    amp.start()

    channel_indices = np.arange(0, amp.CountEeg)

    eeg = None
    while eeg is None:
        eeg = amp.read(
            indices=channel_indices,
            eegcount=len(channel_indices)
        )
    amp.stop()
    amp.close()
    return eeg


# example of obtaining impedance
def get_impedance():
    amp = NeoRec()

    amp.open()
    amp.setup(
        mode=NR_MODE_IMPEDANCE,
        rate=NR_RATE_125HZ,
        range=NR_RANGE_mV300
    )
    amp.start()

    imp = None
    while imp is None:
        imp = amp.readImpedances()
    amp.stop()
    amp.close()
    return imp


if __name__ == "__main__":
    # print(get_eeg_data())
    print(get_impedance())
