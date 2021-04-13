import numpy as np

theta_degre = 45 #pitch
psi_degre   = 20 #yaw
phi_degre   = 15 #roll

def rot_phi(phi_degre): #roll
    phi_rad      = phi_degre / 180 * np.pi
    rotation_mat = np.array([[1,               0,                0],
                             [0, np.cos(phi_rad), -np.sin(phi_rad)],
                             [0, np.sin(phi_rad), np.cos(phi_rad)]])
    
    return rotation_mat

def rot_theta(theta_degre): #pitch
    theta_rad      = theta_degre / 180 * np.pi
    rotation_mat   = np.array([[ np.cos(theta_rad), 0, np.sin(theta_rad)],
                               [                 0, 1,                 0],
                               [-np.sin(theta_rad), 0, np.cos(theta_rad)]])
    
    return rotation_mat

def rot_psi(psi_degre): #yaw
    psi_rad      = psi_degre / 180 * np.pi
    rotation_mat = np.array([[np.cos(psi_rad), -np.sin(psi_rad), 0],
                             [np.sin(psi_rad),  np.cos(psi_rad), 0],
                             [              0,                0, 1]])
    
    return rotation_mat

print(rot_theta(theta_degre)) #pitch
print(rot_psi(psi_degre)) #yaw
print(rot_phi(phi_degre)) #roll

R       = rot_theta(theta_degre) @ rot_psi(psi_degre) @ rot_phi(phi_degre)
P_awal  = np.array([0, 1, 2])
P_akhir = R @ P_awal

print("R = ", R)
print("Posisi Akhir = ", P_akhir)