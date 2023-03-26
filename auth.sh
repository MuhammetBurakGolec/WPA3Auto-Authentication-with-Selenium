alias airport="/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport"

SSID="$1"

# Get the SSID of the current Wi-Fi network
CURRENT_SSID=$(airport -I | awk '/ SSID/ {print $2}')

# Check if the current SSID matches the specified SSID

if [[ "$CURRENT_SSID" = "$SSID" ]]; then
    # If the SSID matches, do nothing

    if ping -q -c 1 -W 1 8.8.8.8 >/dev/null; then
        echo "Connecting to $SSID"
    else
        python ./src/selenium_auth.py
    fi

else
    sudo macchanger -r en0 
    echo "Connecting to $SSID"
    networksetup -setairportnetwork en0 "$SSID"
    python ./src/selenium_auth.py

fi
