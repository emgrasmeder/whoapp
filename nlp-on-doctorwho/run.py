import script_parser

if __name__ == "__main__":
    script = script_parser.Analyzer()
    script.isolate_stage_directions()
    raw_input("isolated stage directions")
    script.isolate_scene_notes()
    script.isolate_speaker()