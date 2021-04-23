cmake_minimum_required(VERSION 3.13)
set(CMAKE_TOOLCHAIN_FILE ${CMAKE_CURRENT_SOURCE_DIR}/../../cmake/stm32_gcc.cmake)

project(stm32-blinky C ASM)
set(CMAKE_INCLUDE_CURRENT_DIR TRUE)

find_package(CMSIS COMPONENTS STM32F1 REQUIRED)
find_package(HAL COMPONENTS STM32F1 RCC GPIO CORTEX REQUIRED)
# Find all drivers:
#find_package(HAL COMPONENTS STM32L0 STM32F1 STM32F4 REQUIRED)
# Find drivers for all families:
#find_package(HAL COMPONENTS RCC GPIO CORTEX REQUIRED)
# Find LL driver:
#find_package(HAL COMPONENTS LL_GPIO REQUIRED)
# Find everything:
#find_package(HAL REQUIRED)


set(TARGET blinky)

add_executable(${TARGET} blinky.c stm32f1xx_hal_conf.h)
target_link_libraries(${TARGET}
    HAL::STM32::F1::RCC
    HAL::STM32::F1::GPIO
    HAL::STM32::F1::CORTEX
    CMSIS::STM32::F103RB
    STM32::NoSys
)

find_program(CMAKE_OBJCOPY NAMES ${STM32_TARGET_TRIPLET}-objcopy PATHS ${TOOLCHAIN_BIN_PATH})
#SET(CMAKE_OBJCOPY ${TOOLCHAIN_BIN_DIR}/${TARGET_TRIPLET}-objcopy CACHE INTERNAL "objcopy tool")

SET(FILENAME "${TARGET}")

ADD_CUSTOM_TARGET(${TARGET}.hex DEPENDS ${TARGET} COMMAND ${CMAKE_OBJCOPY} -Oihex ${FILENAME} ${FILENAME}.hex)
