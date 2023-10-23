set(sample_dir ./src/)
set(target example_tutorial_)

set(sample_pnplib
        ${sample_dir}CsvReader.cpp
        ${sample_dir}CsvWriter.cpp
        ${sample_dir}ModelRegistration.cpp
        ${sample_dir}Mesh.cpp
        ${sample_dir}Model.cpp
        ${sample_dir}PnPProblem.cpp
        ${sample_dir}Utils.cpp
        ${sample_dir}RobustMatcher.cpp
)

include_directories(${OPENCV_CPP_SAMPLES_REQUIRED_DEPS})

add_executable( ${target}pnp_registration ${sample_dir}main_registration.cpp ${sample_pnplib} )
add_executable( ${target}pnp_detection ${sample_dir}main_detection.cpp ${sample_pnplib} )

target_link_libraries(${target}pnp_registration PRIVATE ${OPENCV_LINKER_LIBS} ${OPENCV_CPP_SAMPLES_REQUIRED_DEPS})
target_link_libraries(${target}pnp_detection PRIVATE ${OPENCV_LINKER_LIBS} ${OPENCV_CPP_SAMPLES_REQUIRED_DEPS})
