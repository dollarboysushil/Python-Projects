from winotify import Notification, audio


toast = Notification(
    app_id="Alert", title="Community Meeting Starting Soon!", msg="JOIN ASAP", duration="short")


toast.set_audio(audio.SMS, loop=True)
toast.add_actions(label="Github",
                  launch="https://github.com/dollarboysushil")
toast.add_actions(label="Youtube",
                  launch="https://youtube.com/dollarboysushil")
toast.show()
