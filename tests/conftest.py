from tests.fixtures.browsers import *  # noqa: F401 F403
from tests.fixtures.factories import *  # noqa: F401 F403
from tests.fixtures.pages import *  # noqa: F401 F403
from tests.fixtures.play_ground_pages import *  # noqa: F401 F403


def pytest_configure(config) -> None:
    config.addinivalue_line('markers', 'regression: marker for regression tests')
    config.addinivalue_line('markers', 'ajax_data_page: marker for ajax_data_page tests')
    config.addinivalue_line('markers', 'class_attribute_page: marker for class_attribute_page tests')
    config.addinivalue_line('markers', 'click_page: marker for click_page tests')
    config.addinivalue_line('markers', 'client_side_delay_page: marker for client_side_delay_page tests')
    config.addinivalue_line('markers', 'hidden_layers_page: marker for hidden_layers_page tests')
    config.addinivalue_line('markers', 'load_delay_page: marker for load_delay_page tests')
    config.addinivalue_line('markers', 'main_page: marker for main_page tests')
    config.addinivalue_line('markers', 'mouse_over_page: marker for mouse_over_page tests')
    config.addinivalue_line('markers', 'non_breaking_space_page: marker for non_breaking_space_page tests')
    config.addinivalue_line('markers', 'overlapped_element_page: marker for overlapped_element_page tests')
    config.addinivalue_line('markers', 'progress_bar_page: marker for progress_bar_page tests')
    config.addinivalue_line('markers', 'sample_app_page: marker for sample_app_page tests')
    config.addinivalue_line('markers', 'scrollbars_page: marker for scrollbars_page tests')
    config.addinivalue_line('markers', 'text_input_page: marker for text_input_page tests')
    config.addinivalue_line('markers', 'verify_text_page: marker for verify_text_page tests')
    config.addinivalue_line('markers', 'dynamic_table_page: marker for dynamic_table_page tests')
