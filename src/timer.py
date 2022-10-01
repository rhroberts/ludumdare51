from config import FPS


class Timer:
    # callbacks: List[Callable] = []

    # @classmethod
    # def register_ten_second_callback(cls, func: Callable):
    #     cls.callbacks.add(func)

    started = False
    frame_count = 0;
    is_ten_seconds = False;

    @classmethod
    def start(cls):
        cls.started = True

    @classmethod
    def update(cls):
        if not cls.started:
            return

        # Assumption is this is called once per frame
        cls.frame_count += 1

        if (cls.frame_count / FPS) == 10:
            cls.is_ten_seconds = True
            cls.frame_count = 0
        else:
            cls.is_ten_seconds = False

    @classmethod
    def is_ten_seconds(cls):
        """Returns true if this frame falls on a ten second interval, else false"""
        if not cls.started:
            raise RuntimeError("You never started the timer.")
        return cls.is_ten_seconds
