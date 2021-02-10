from pathlib import Path
from os import path
from zeppos_logging.app_logger import AppLogger


class Root:
    @staticmethod
    def find_root_of_project(current_module_filename,
                             root_marker_filename_list=[".root", "manage.py", "Pipfile"]):
        AppLogger.logger.debug(f"current_module_filename: {current_module_filename}")
        AppLogger.logger.debug(f"root_marker_filename_list: {root_marker_filename_list}")
        for root_marker_filename in root_marker_filename_list:
            root_path = Root._get_root_directory_using_root_marker_file(
                directory=Root.get_path_object_of_full_file_name(
                    current_module_filename
                ),
                root_marker_filename=root_marker_filename,
                loop_counter=1
            )
            if root_path:
                AppLogger.logger.debug(f"root_path: {root_path}")
                return root_path
        AppLogger.logger.debug(f"root_path: None")
        return None

    @staticmethod
    def get_real_path(partial_full_filename):
        return path.realpath(partial_full_filename)

    @staticmethod
    def get_path_object_of_full_file_name(full_file_name):
        return \
            Path(
                Root.get_real_path(
                    full_file_name
                )
            )

    @staticmethod
    def _get_root_directory_using_root_marker_file(directory, root_marker_filename, loop_counter):
        try:
            while True:
                full_file_name_list = list(directory.glob(root_marker_filename))
                if len(full_file_name_list) > 0:
                    return path.dirname(full_file_name_list[0])

                loop_counter += 1
                if loop_counter > 50:
                    return None

                return Root._get_root_directory_using_root_marker_file(directory.parent, root_marker_filename,
                                                                       loop_counter)
            return None
        except:
            return None
