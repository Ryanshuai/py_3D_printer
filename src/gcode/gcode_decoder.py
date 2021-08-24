class Decoder:
    def distribute(self, code):
        code = code.replace('\n', '')
        if code.startswith(";"):
            return
        code = code.split(";")[0]

        if code.startswith("G"):
            self.g_code_decode(code)

        if code.startswith("M"):
            self.m_code_decode(code)

    def m_code_decode(self, code):
        code_head = code.split(" ")[0]

        if code_head == "M82":
            self.extrude = "abs"

        elif code_head == "M84":
            _, *time = code.split(" ")
            time = float(time[1:]) if time else 0
            self.stepper_turn_off_in = time

        elif code_head == "M104":
            _, nozzle_temp = code.split(" ")
            nozzle_temp = int(nozzle_temp[1:])
            print("nozzle_temp", nozzle_temp)

        elif code_head == "M105":
            pass

        elif code_head == "M109":
            _, nozzle_temp = code.split(" ")
            nozzle_temp = int(nozzle_temp[1:])
            print("nozzle_temp", nozzle_temp)

        elif code_head == "M140":
            _, bed_temp = code.split(" ")
            bed_temp = int(bed_temp[1:])
            print("bed_temp", bed_temp)

        elif code_head == "M190":
            _, bed_temp = code.split(" ")
            bed_temp = int(bed_temp[1:])
            print("bed_temp", bed_temp)

        elif code_head == "M106":
            _, fan_speed = code.split(" ")
            fan_speed = int(fan_speed[1:])
            print("fan_speed", fan_speed)

        elif code_head == "M107":
            fan_speed = 0
            print("fan_speed", 0)

        else:
            raise Exception(code)

    def g_code_decode(self, code):
        code_head = code.split(" ")[0]

        if code_head =="G0":
            _, *moves = code.split(" ")
            x_move, y_move, f_speed, e_move = 0, 0, 0, 0
            for move in moves:
                if move.startswith("X"):
                    x_move = float(move[1:])
                elif move.startswith("Y"):
                    y_move = float(move[1:])
                elif move.startswith("F"):
                    f_speed = float(move[1:])
                elif move.startswith("E"):
                    e_move = float(move[1:])
            print("move: ", x_move, y_move, f_speed, e_move)

        elif code_head =="G1":
            _, *moves = code.split(" ")
            x_move, y_move, f_speed, e_move = 0, 0, 0, 0
            for move in moves:
                if move.startswith("X"):
                    x_move = float(move[1:])
                elif move.startswith("Y"):
                    y_move = float(move[1:])
                elif move.startswith("F"):
                    f_speed = float(move[1:])
                elif move.startswith("E"):
                    e_move = float(move[1:])
            print("move: ", x_move, y_move, f_speed, e_move)

        elif code_head =="G2":
            pass

        elif code_head =="G3":
            pass

        elif code_head =="G17":
            self.platform = "xy"
            print("platform: ", self.platform)

        elif code_head == "G18":
            self.platform = "zx"
            print("platform: ", self.platform)

        elif code_head == "G19":
            self.platform = "yz"
            print("platform: ", self.platform)

        elif code_head == "G20":
            self.unit = "inch"

        elif code_head == "G21":
            self.unit = "mm"

        elif code_head == "G28":
            # move to zero
            pass

        elif code_head == "G90":
            pass

        elif code_head == "G91":
            pass

        elif code_head == "G92":
            _, extrude_resolution = code.split(" ")
            self.extrude_resolution = extrude_resolution

        else:
            raise Exception(code)


if __name__ == '__main__':
    with open("CFFFP_111.gcode", "r") as f:
        lines = f.readlines()

    for line in lines:
        decoder = Decoder()
        decoder.distribute(line)
