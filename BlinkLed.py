+# -*- coding: utf-8-*-
+import random
+import re
+import RPi.GPIO as GPIO
+import time
+import os
+
+WORDS = ["LIGHT","LED"]
+
+def blink(pin):
+        os.system("sudo gpio write 0 1")
+        time.sleep(1)
+        os.system("sudo gpio write 0 0")
+        time.sleep(1)
+        return
+
+def handle(text, mic, profile):
+    """
+        Arguments:
+        text -- user-input, typically transcribed speech
+        mic -- used to interact with the user (for both input and output)
+        profile -- contains information related to the user (e.g., phone
+                   number)
+    """
+    messages = ["Led on."]
+
+    message = random.choice(messages)
+
+    mic.say(message)
+    # blink GPIO17 50 times
+    for i in range(0,5):
+            blink(11)
+
+
+def isValid(text):
+    """
+        Arguments:
+        text -- user-input, typically transcribed speech
+    """
+    return bool(re.search(r'\b(light|led)\b', text, re.IGNORECASE))
