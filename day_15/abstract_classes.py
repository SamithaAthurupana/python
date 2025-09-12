from abc import ABC, abstractmethod


class Notifier(ABC):

    @abstractmethod
    def send(self, message: str) -> None:
        pass

class EmailNotifier(Notifier):

    def send(self, message: str) -> None:
        print("Sending an Email") # මෙය abstract method එකට අදාළ concrete implementation එක.

class SendNotifier(Notifier):

    def send(self, message: str) -> None:
        if message is not None:
            print(f"Sending Message {message}")

    def notify(notifier: Notifier, message: str) -> None:
        notifier.send(message)


email = EmailNotifier()
email.send("sdasds")

s = SendNotifier()
s.notify("Hi")   # -> Sending an Email
s.notify("Hello") # -> Sending Message Hello


